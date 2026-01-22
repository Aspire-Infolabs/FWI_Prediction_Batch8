// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const html = document.documentElement;

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
html.setAttribute('data-theme', savedTheme);
updateThemeIcon(savedTheme);

themeToggle.addEventListener('click', () => {
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
});

function updateThemeIcon(theme) {
    themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
}

// Scroll to form
function scrollToForm() {
    document.getElementById('formSection').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

// Sync range and number inputs
const inputPairs = [
    { number: 'Temperature', slider: 'TemperatureSlider' },
    { number: 'RH', slider: 'RHSlider' },
    { number: 'Ws', slider: 'WsSlider' },
    { number: 'Rain', slider: 'RainSlider' },
    { number: 'FFMC', slider: 'FFMCSlider' },
    { number: 'DMC', slider: 'DMCSlider' },
    { number: 'DC', slider: 'DCSlider' },
    { number: 'ISI', slider: 'ISISlider' },
    { number: 'BUI', slider: 'BUISlider' }
];

inputPairs.forEach(pair => {
    const numberInput = document.getElementById(pair.number);
    const sliderInput = document.getElementById(pair.slider);

    if (numberInput && sliderInput) {
        // Sync slider to number input
        sliderInput.addEventListener('input', () => {
            numberInput.value = sliderInput.value;
        });

        // Sync number input to slider
        numberInput.addEventListener('input', () => {
            const value = parseFloat(numberInput.value);
            const min = parseFloat(sliderInput.min);
            const max = parseFloat(sliderInput.max);
            
            if (value >= min && value <= max) {
                sliderInput.value = value;
            } else if (value < min) {
                numberInput.value = min;
                sliderInput.value = min;
            } else if (value > max) {
                numberInput.value = max;
                sliderInput.value = max;
            }
        });
    }
});

// Reset Form
function resetForm() {
    const form = document.getElementById('predictionForm');
    form.reset();
    
    // Reset to default values (matching dataset example)
    const defaults = {
        'Temperature': 29,
        'RH': 57,
        'Ws': 18,
        'Rain': 0.0,
        'FFMC': 65.7,
        'DMC': 3.4,
        'DC': 7.6,
        'ISI': 1.3,
        'BUI': 3.4
    };
    
    Object.keys(defaults).forEach(key => {
        const numberInput = document.getElementById(key);
        const sliderInput = document.getElementById(key + 'Slider');
        if (numberInput) numberInput.value = defaults[key];
        if (sliderInput) sliderInput.value = defaults[key];
    });
}

// FWI Prediction using Ridge Model API
async function predictFWI(formData) {
    try {
        // Call Flask API endpoint
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success && data.fwi !== undefined) {
            console.log('Prediction received from API:', data.fwi);
            return parseFloat(data.fwi);
        } else {
            // Fallback to dummy calculation if API fails
            console.warn('API error, using fallback calculation:', data.error);
            return fallbackFWI(formData);
        }
    } catch (error) {
        // Fallback to dummy calculation if API is not available
        console.warn('API not available, using fallback calculation:', error);
        return fallbackFWI(formData);
    }
}

// Fallback FWI calculation (used when API is unavailable)
function fallbackFWI(formData) {
    const temp = parseFloat(formData.Temperature) || 0;
    const humidity = parseFloat(formData.RH) || 0;
    const windSpeed = parseFloat(formData.Ws) || 0;
    const rain = parseFloat(formData.Rain) || 0;
    const ffmc = parseFloat(formData.FFMC) || 0;
    const dmc = parseFloat(formData.DMC) || 0;
    const dc = parseFloat(formData.DC) || 0;
    const isi = parseFloat(formData.ISI) || 0;
    const bui = parseFloat(formData.BUI) || 0;

    // Simplified FWI calculation (fallback)
    let fwi = 0;
    
    fwi += (temp / 50) * 20;
    fwi += ((100 - humidity) / 100) * 15;
    fwi += (windSpeed / 100) * 25;
    fwi -= (rain / 50) * 10;
    fwi += (ffmc / 101.2) * 10;
    fwi += (dmc / 800) * 10;
    fwi += (dc / 800) * 5;
    fwi += (isi / 56) * 3;
    fwi += (bui / 800) * 2;

    fwi = Math.max(0, Math.min(100, fwi));
    
    return fwi;
}

// Determine Fire Classification based on FWI value
// Based on dataset analysis: FWI >= 2.5 typically indicates "fire"
// Threshold adjusted based on dataset patterns
function getFireClassification(fwi) {
    // Threshold: FWI >= 2.5 is typically "fire", < 2.5 is "not fire"
    // Some edge cases exist, but this is the general pattern
    const threshold = 2.5;
    const isFire = fwi >= threshold;
    
    return {
        classification: isFire ? 'fire' : 'not fire',
        label: isFire ? 'Fire' : 'Not Fire',
        icon: isFire ? '🔥' : '✅',
        color: isFire ? '#e53e3e' : '#48bb78'
    };
}

// Draw Gauge Chart
function drawGauge(canvas, value, maxValue = 100) {
    const ctx = canvas.getContext('2d');
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = Math.min(centerX, centerY) - 20;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw background arc
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, Math.PI, 0, false);
    ctx.lineWidth = 20;
    ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--bg-primary').trim();
    ctx.stroke();
    
    // Calculate angle based on value
    const percentage = value / maxValue;
    const angle = Math.PI - (Math.PI * percentage);
    
    // Determine color based on value
    let color;
    if (value < 5) color = '#48bb78'; // green
    else if (value < 20) color = '#ed8936'; // yellow
    else if (value < 40) color = '#f56565'; // orange
    else color = '#e53e3e'; // red
    
    // Draw value arc
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, Math.PI, angle, true);
    ctx.lineWidth = 20;
    ctx.strokeStyle = color;
    ctx.lineCap = 'round';
    ctx.stroke();
    
    // Draw tick marks
    for (let i = 0; i <= 10; i++) {
        const tickAngle = Math.PI - (Math.PI * (i / 10));
        const x1 = centerX + (radius + 10) * Math.cos(tickAngle);
        const y1 = centerY + (radius + 10) * Math.sin(tickAngle);
        const x2 = centerX + (radius + 20) * Math.cos(tickAngle);
        const y2 = centerY + (radius + 20) * Math.sin(tickAngle);
        
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.lineWidth = 2;
        ctx.strokeStyle = getComputedStyle(document.documentElement).getPropertyValue('--text-secondary').trim();
        ctx.stroke();
    }
}

// Update Results Display
function updateResults(fwi) {
    const fireClass = getFireClassification(fwi);
    const outputCard = document.getElementById('outputCard');
    const resultsContainer = document.getElementById('resultsContainer');
    
    // Ensure FWI is a valid number
    if (isNaN(fwi) || fwi === null || fwi === undefined) {
        console.error('Invalid FWI value:', fwi);
        fwi = 0;
    }
    
    // Ensure FWI is non-negative (in case model predicts negative)
    if (fwi < 0) {
        fwi = 0;
    }
    
    // Update FWI value (show appropriate decimal places)
    // For values < 1, show 2 decimals; for >= 1, show 1 decimal
    const fwiDisplay = fwi < 1 ? fwi.toFixed(2) : fwi.toFixed(1);
    document.getElementById('fwiValue').textContent = fwiDisplay;
    
    // Update fire classification display
    const riskLevel = document.getElementById('riskLevel');
    riskLevel.className = `risk-level ${fireClass.classification}`;
    riskLevel.innerHTML = `
        <span class="risk-icon">${fireClass.icon}</span>
        <span class="risk-text" style="color: ${fireClass.color};">${fireClass.label}</span>
    `;
    
    // Update classification result display - show "fire" or "not fire"
    const classificationResult = document.getElementById('classificationResult');
    if (classificationResult) {
        classificationResult.textContent = fireClass.classification === 'fire' ? 'fire' : 'not fire';
        classificationResult.style.color = fireClass.color;
        classificationResult.style.fontSize = '2rem';
        classificationResult.style.fontWeight = '700';
    }
    
    // Draw gauge (use max 50 for better visualization of typical FWI range)
    const canvas = document.getElementById('fwiGauge');
    drawGauge(canvas, fwi, 50);
    
    // Show results with animation
    outputCard.classList.add('show');
    resultsContainer.style.animation = 'slideIn 0.5s ease';
    
    // Log for debugging
    console.log('FWI Prediction:', {
        fwi: fwiDisplay,
        classification: fireClass.classification,
        label: fireClass.label
    });
}

// Form Submission
const form = document.getElementById('predictionForm');
const predictBtn = document.getElementById('predictBtn');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Get form data with correct field names matching dataset
    const formData = {
        Temperature: parseFloat(document.getElementById('Temperature').value) || 0,
        RH: parseFloat(document.getElementById('RH').value) || 0,
        Ws: parseFloat(document.getElementById('Ws').value) || 0,
        Rain: parseFloat(document.getElementById('Rain').value) || 0,
        FFMC: parseFloat(document.getElementById('FFMC').value) || 0,
        DMC: parseFloat(document.getElementById('DMC').value) || 0,
        DC: parseFloat(document.getElementById('DC').value) || 0,
        ISI: parseFloat(document.getElementById('ISI').value) || 0,
        BUI: parseFloat(document.getElementById('BUI').value) || 0
    };
    
    // Show loading state
    predictBtn.classList.add('loading');
    predictBtn.disabled = true;
    
    try {
        // Predict FWI using Ridge model API
        const fwi = await predictFWI(formData);
        
        // Validate FWI value
        if (isNaN(fwi) || fwi === null || fwi === undefined) {
            throw new Error('Invalid FWI prediction received');
        }
        
        // Update results
        updateResults(fwi);
        
        // Scroll to results
        document.getElementById('outputSection').scrollIntoView({ 
            behavior: 'smooth',
            block: 'start'
        });
    } catch (error) {
        console.error('Prediction error:', error);
        alert('Error making prediction. Please check console for details.');
    } finally {
        // Reset button state
        predictBtn.classList.remove('loading');
        predictBtn.disabled = false;
    }
});

// Initialize gauge on load
window.addEventListener('load', () => {
    const canvas = document.getElementById('fwiGauge');
    drawGauge(canvas, 0);
});

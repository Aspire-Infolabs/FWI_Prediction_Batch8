from flask import Flask, render_template, request
import pickle
import os
import numpy as np

# Initialize Flask app FIRST to avoid NameError
app = Flask(__name__)

# Define base directory for file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the model and scaler using absolute paths 
model = pickle.load(open(os.path.join(BASE_DIR, 'ridge.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb'))

@app.route('/')
def home():
    """Renders the main input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles form submission, scaling, and prediction."""
    try:
        # 1. Extract features from form in the exact order required by the model
        # Note: If your model was trained on 7 or 8 features, adjust this list
        feature_keys = ['Temperature', 'RH', 'Wind', 'Rain', 'FFMC', 'DMC', 'DC', 'BUI', 'ISI']
        
        # Convert form values to floats 
        raw_values = [float(request.form[x]) for x in feature_keys]
        
        # 2. Scale the data using the pre-loaded StandardScaler 
        scaled_data = scaler.transform([raw_values])
        
        # 3. Generate prediction [cite: 3]
        prediction = model.predict(scaled_data)
        fwi = prediction[0]
        
        # Debugging: Print to console to see the raw FWI value
        print(f"Calculated FWI: {fwi}")

        # 4. Logic for Risk Categorization
        if fwi <= 7: 
            risk = "Low 🔵"
        elif fwi <= 16: 
            risk = "Moderate 🟡"
        elif fwi <= 31: 
            risk = "High 🟠"
        else: 
            risk = "Extreme 🔴"

        return render_template('index.html', prediction=round(fwi, 2), risk=risk)
    
    except Exception as e:
        return f"An error occurred: {str(e)}. Please check your input values."

if __name__ == '__main__':
    app.run(debug=True)

function predictFWI(){
  const data = {
    ISI: parseFloat(document.getElementById("isi").value),
    DMC: parseFloat(document.getElementById("dmc").value),
    BUI: parseFloat(document.getElementById("bui").value),
    DC: parseFloat(document.getElementById("dc").value),
    FFMC: parseFloat(document.getElementById("ffmc").value),
    Temperature: parseFloat(document.getElementById("temp").value),
    Rain: parseFloat(document.getElementById("rain").value),
    RH: parseFloat(document.getElementById("rh").value),
    Ws: parseFloat(document.getElementById("ws").value)
  };

 
  fetch("/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(result => {
    const fwi = result.fwi;
    document.getElementById("fwi").innerText = fwi;

    const risk = document.getElementById("risk");
    const alertBox = document.getElementById("alert");
    const explain = document.getElementById("explain");
    const fwival = document.getElementById("fwi");

    if (fwi < 20) {
    fwival.style.color = "green";
    risk.innerText = "LOW RISK";
    risk.style.background = "green";
    alertBox.style.display = "none";

  explain.innerHTML = `
    • Fire ignition is unlikely<br>
    • Any small fire remains controllable<br>
    • Normal outdoor and forest activities are safe`;

} else if (fwi < 40) {
  fwival.style.color = "orange";
  risk.innerText = "MODERATE RISK";
  risk.style.background = "orange";
  alertBox.style.display = "none";

  explain.innerHTML = `
    • Fires may start and spread under favorable conditions<br>
    • Fire control may require quick response<br>
    • Caution is advised for outdoor activities
  `;

} else {
  fwival.style.color = "red";
  risk.innerText = "EXTREME RISK";
  risk.style.background = "red";
  alertBox.style.display = "block";

  explain.innerHTML = `
    • Fires can ignite easily and spread rapidly<br>
    • Large, intense fires are difficult to control<br>
    • Serious threat to life, property, and environment
  `;
}
    updateRiskVisual(fwi);
  })
  .catch(err => console.error("Prediction error:", err));
}

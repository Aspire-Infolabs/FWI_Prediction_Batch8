
from turtle import color
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
with open("ridge.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    FEATURE_ORDER = [
        'Temperature',
        'RH',
        'Rain',
        'FFMC',
        'DMC',
        'DC',
        'ISI',
        'BUI',
        'Ws'
    ]

    # Collect inputs in EXACT training order
    features = [float(request.form[f]) for f in FEATURE_ORDER]

    input_data = np.array(features).reshape(1, -1)

    # Sanity check (important for debugging)
    assert input_data.shape[1] == 9

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Predict FWI
    prediction = model.predict(scaled_data)[0]
    fwi_value = round(float(prediction), 2)

    # Risk classification
    if fwi_value < 5:
        risk = "Low"
        color = "low"
    elif fwi_value < 12:
        risk = "Moderate"
        color = "moderate"
    elif fwi_value < 25:
        risk = "High"
        color = "high"
    else:
        risk = "Extreme"
        color = "extreme"

    return render_template(
        "home.html",
        prediction=fwi_value,
        risk=risk,
        color=color
    )
if __name__ == "__main__":
    app.run(debug=True) 
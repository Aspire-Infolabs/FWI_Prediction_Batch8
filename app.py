from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load scaler and model
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("ridge.pkl", "rb") as f:
    model = pickle.load(f)

# feature names
FEATURES = [
    "Temperature", "RH", "Ws", "Rain",
    "FFMC", "DMC", "DC", "ISI", "BUI"
]

def fwi_category(fwi):
    if fwi <= 5:
        return "Low"
    elif fwi <= 11:
        return "Moderate"
    elif fwi <= 21:
        return "High"
    elif fwi <= 33:
        return "Very High"
    else:
        return "Extreme"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read inputs IN CORRECT ORDER
        input_values = [float(request.form[f]) for f in FEATURES]

        X = np.array([input_values])
        X_scaled = scaler.transform(X)
        prediction = model.predict(X_scaled)[0]

        return render_template(
            "home.html",
            prediction=round(float(prediction), 2),
            category=fwi_category(prediction)
        )

    except Exception as e:
        return f"Prediction error: {e}"

if __name__ == "__main__":
    app.run(debug=True)

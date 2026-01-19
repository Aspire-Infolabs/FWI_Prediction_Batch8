
from flask import Flask, render_template, request
import pickle
import numpy as np


# 1. Create Flask App

app = Flask(__name__)


# 2. Load Model & Scaler

with open("ridge.pkl", "rb") as f:
    model_data = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

coef = model_data["coef_"]
intercept = model_data["intercept_"]


SCALER_KEYS = list(scaler.keys())
print("SCALER KEYS >>>", SCALER_KEYS)


# 3. Home Route

@app.route("/")
def home():
    return render_template("predict.html")


# 4. Prediction Route

@app.route("/predict", methods=["POST"])
def predict():
    try:

        form_values = {
            "Temperature": float(request.form["Temperature"]),
            "RH": float(request.form["RH"]),
            "WS": float(request.form["WS"]),
            "Rain": float(request.form["Rain"]),
            "FFMC": float(request.form["FFMC"]),
            "DMC": float(request.form["DMC"]),
            "DC": float(request.form["DC"]),
            "ISI": float(request.form["ISI"]),
            "BUI": float(request.form["BUI"])
        }

        scaled_values = []
        for key in SCALER_KEYS:
            key_lower = key.lower()

            if "temp" in key_lower:
                value = form_values["Temperature"]
            elif key_lower == "rh":
                value = form_values["RH"]
            elif "ws" in key_lower or "wind" in key_lower:
                value = form_values["WS"]
            elif "rain" in key_lower:
                value = form_values["Rain"]
            elif "ffmc" in key_lower:
                value = form_values["FFMC"]
            elif "dmc" in key_lower:
                value = form_values["DMC"]
            elif key_lower == "dc":
                value = form_values["DC"]
            elif "isi" in key_lower:
                value = form_values["ISI"]
            elif "bui" in key_lower:
                value = form_values["BUI"]
            else:
                raise Exception(f"Unknown scaler key: {key}")

            mean = scaler[key]["mean"]
            std = scaler[key]["std"]
            scaled_values.append((value - mean) / std)

        X = np.array(scaled_values)
        prediction = np.dot(X, coef) + intercept

        return render_template(
            "result.html",
            prediction=round(float(prediction), 2)
        )

    except Exception as e:
        return f"Error: {e}"
# 5. Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

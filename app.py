from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)


with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/ridge.pkl", "rb") as f:
    ridge = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [
        data["ISI"], data["DMC"], data["BUI"], data["DC"],
        data["FFMC"], data["Temperature"], data["Rain"],
        data["RH"], data["Ws"]
    ]
    X = np.array(features).reshape(1, -1)

    X_scaled = scaler.transform(X)
    
    fwi_pred = ridge.predict(X_scaled)[0]
    fwi_pred = round(max(0, fwi_pred), 1)  

    return jsonify({"fwi": fwi_pred})

if __name__ == "__main__":
    app.run(debug=True)

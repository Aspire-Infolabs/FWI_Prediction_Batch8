from flask import Flask, render_template, request
import numpy as np
import pickle
from flask import Flask, send_from_directory

app = Flask(__name__)
model = pickle.load(open("ridge.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form['Temperature']),
        float(request.form['RH']),
        float(request.form['Ws']),
        float(request.form['Rain']),
        float(request.form['FFMC']),
        float(request.form['DMC']),
        float(request.form['DC']),
        float(request.form['ISI']),
        float(request.form['BUI']),
    ]

    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)[0]
    
    if prediction < 5:
        risk = "Low"
        risk_class = "low"
    elif prediction < 15:
        risk = "Moderate"
        risk_class = "moderate"
    elif prediction < 30:
        risk = "High"
        risk_class = "high"
    else:
        risk = "Extreme"
        risk_class = "extreme"
    
    return render_template(
        "output.html",
        prediction=round(prediction, 2),
        risk=risk,
        risk_class=risk_class
    )

@app.route('/fwi_image.jpg')
def bg_image():
    return send_from_directory('.', 'fwi_image.jpg')

if __name__ == "__main__":
    app.run(debug=True)

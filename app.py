from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("ridge_tuned.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["Temperature"]),
        float(request.form["RH"]),
        float(request.form["Ws"]),
        float(request.form["Rain"]),
        float(request.form["FFMC"]),
        float(request.form["DMC"]),
        float(request.form["DC"]),
        float(request.form["ISI"]),
        float(request.form["Region_encoded"])
    ]

    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    return render_template(
        "predict.html",
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)

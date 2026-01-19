from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('ridge.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    temperature = float(request.form['temperature'])
    rh = float(request.form['rh'])
    wind = float(request.form['wind'])
    rain = float(request.form['rain'])
    ffmc = float(request.form['ffmc'])
    dmc = float(request.form['dmc'])
    isi = float(request.form['isi'])
    region = float(request.form['region'])

    # Convert input to numpy array
    input_data = np.array([[temperature, rh, wind, rain, ffmc, dmc, isi, region]])

    # Scale input data
    input_scaled = scaler.transform(input_data)

    # Predict Fire Weather Index (FWI)
    prediction = model.predict(input_scaled)[0]
    prediction = round(prediction, 2)

    if prediction < 7:
        risk = "Low Fire Risk"
        badge = "low"
    elif prediction < 15:
        risk = "Moderate Fire Risk"
        badge = "moderate"
    else:
        risk = "High Fire Risk"
        badge = "high"

    return render_template(
        'home.html',
        prediction=prediction,
        risk=risk,
        badge=badge
    )

if __name__ == "__main__":
    app.run(debug=True)
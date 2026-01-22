from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

def risk_level(fwi):
    if fwi < 5.2:
        return "Very Low"
    elif fwi < 11.2:
        return "Low"
    elif fwi < 21.3:
        return "Moderate"
    elif fwi < 38.0:
        return "High"
    elif fwi <= 50:
        return "Very High"
    else:
        return "Extreme"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    values = [
        float(request.form['Temperature']),
        float(request.form['RH']),
        float(request.form['Ws']),
        float(request.form['Rain']),
        float(request.form['FFMC']),
        float(request.form['DMC']),
        float(request.form['DC']),
        float(request.form['ISI']),
        float(request.form['BUI'])
        
    ]

    arr = np.array(values).reshape(1, -1)
    scaled = scaler.transform(arr)
    prediction = model.predict(scaled)[0]
    level = risk_level(prediction)

    return render_template(
        'home.html',
        prediction=round(prediction, 2),
        level=level
    )

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture the 9 inputs from input.html
    input_features = [float(x) for x in request.form.values()]
    
    # Placeholder for calculation (Replace with your model.predict if you have a .pkl file)
    prediction = sum(input_features) / len(input_features) 

    # Logic for all risk levels including Extreme
    if prediction < 11.2:
        risk = "Low"
    elif 11.2 <= prediction < 21.3:
        risk = "Moderate"
    elif 21.3 <= prediction < 50.0:
        risk = "High"
    else:
        risk = "Extreme"

    return render_template('result.html', prediction=round(prediction, 2), risk=risk)

if __name__ == "__main__":
    app.run(debug=True)
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
    # This captures the data from your input.html form
    data = [float(x) for x in request.form.values()]
    # Note: You would normally load a 'model.pkl' here to make a real prediction
    prediction = sum(data) / len(data) # Placeholder logic
    risk = "Low" if prediction < 10 else "High"
    
    return render_template('result.html', prediction=round(prediction, 2), risk=risk)

if __name__ == '__main__':
    app.run(debug=True)
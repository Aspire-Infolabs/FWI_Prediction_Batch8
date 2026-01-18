
from flask import Flask, render_template, request
import pickle, os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR,'ridge.pkl'),'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR,'scaler.pkl'),'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = [float(request.form[x]) for x in
        ['Temperature','RH','Wind','Rain','FFMC','DMC','DC','BUI','ISI']]

    fwi = model.predict(scaler.transform([values]))[0]

    if fwi <= 7: risk = "Low 🔵"
    elif fwi <= 16: risk = "Moderate 🟡"
    elif fwi <= 31: risk = "High 🟠"
    else: risk = "Extreme 🔴"

    return render_template('index.html', prediction=round(fwi,2), risk=risk)

if __name__ == '__main__':
    app.run(debug=True)

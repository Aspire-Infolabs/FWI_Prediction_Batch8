from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('ridge.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            Temperature = float(request.form['Temperature'])
            RH = float(request.form['RH'])
            Ws = float(request.form['Ws'])
            Rain = float(request.form['Rain'])
            FFMC = float(request.form['FFMC'])
            DMC = float(request.form['DMC'])
            DC = float(request.form['DC'])
            ISI = float(request.form['ISI'])
            BUI = float(request.form['BUI'])

            # IMPORTANT: SAME ORDER AS TRAINING
            input_data = np.array([[Temperature, RH, Ws, Rain,
                                    FFMC, DMC, DC, ISI, BUI]])

            scaled_data = scaler.transform(input_data)
            prediction = model.predict(scaled_data)[0]

            return render_template('home.html', result=round(prediction, 2))

        except Exception as e:
            return f"Error: {e}"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)






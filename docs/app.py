@app.route('/predict', methods=['POST'])
def predict():
    # 1. Collect and convert to float
    feature_list = ['Temperature','RH','Wind','Rain','FFMC','DMC','DC','BUI','ISI']
    input_data = [float(request.form[x]) for x in feature_list] [cite: 1]

    # 2. Transform the data
    scaled_data = scaler.transform([input_data]) [cite: 1]
    
    # DEBUG: See what the scaler is doing in your terminal
    print(f"Scaled Values: {scaled_data}")

    # 3. Predict
    prediction = model.predict(scaled_data) [cite: 1, 3]
    fwi = prediction[0] [cite: 1]

    # 4. Logic for Risk
    if fwi <= 7: risk = "Low 🔵"
    elif fwi <= 16: risk = "Moderate 🟡"
    elif fwi <= 31: risk = "High 🟠"
    else: risk = "Extreme 🔴" [cite: 1]

    return render_template('index.html', prediction=round(fwi,2), risk=risk) [cite: 1]

# FWI Predictor - Forest Fire Weather Index Prediction System


The **FWI Predictor** is a machine learning-based system designed to predict the Forest Fire Weather Index (FWI) using weather and forest condition data. This project combines data preprocessing, exploratory data analysis (EDA), machine learning modeling, and a web-based interface for making predictions on forest fire risk.


## Input Features
- **Temperature**: Air temperature (°C)
- **RH**: Relative humidity (%)
- **Ws**: Wind speed (km/h)
- **Rain**: Total rainfall (mm)
- **FFMC**: Fine Fuel Moisture Code
- **DMC**: Duff Moisture Code
- **DC**: Drought Code
- **ISI**: Initial Spread Index
- **Region**: Geographic region (encoded numerically)

# Target Variable
- **FWI**: Forest Fire Weather Index (numerical value indicating fire danger level)

# Technical Stack

- **Python 3.11+**
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Visualization**: matplotlib, seaborn
- **Web Framework**: Flask, Flask-CORS
- **Data Serialization**: pickle

# Workflow

![alt text](FWI.png)

# Installation and Setup

1. Clone or Extract the Project

2. Create and Activate Virtual Environment

Windows
python -m venv env
env\Scripts\activate

Linux/macOS
python -m venv env
source env/bin/activate

3. Install Dependencies

pip install -r requirements.txt
pip install flask flask-cors

4.Running the Web Application

python app.py

Then navigate to `http://localhost:5000` in your browser to use the prediction interface.

# Web Application Output Screens

index.html
![alt text](indexpage.png)

predict.html
![alt text](<predict page.png>)

# conclusion
This project presents a Fire Weather Index (FWI) Prediction System using machine learning and Flask to assess forest fire risk based on key meteorological and fuel parameters. A Ridge Regression model was used to ensure stable and accurate predictions through effective preprocessing and feature scaling. The system demonstrates how machine learning and web technologies can support early fire risk assessment and environmental disaster prevention.



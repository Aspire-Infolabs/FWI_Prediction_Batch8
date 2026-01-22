🔥 Fire Weather Index (FWI) Predictor

A Machine Learning–based web application that predicts the Fire Weather Index (FWI) using environmental and fire-danger parameters. The system helps assess wildfire risk levels and supports early warning and decision-making for forest fire management.

📌 Project Overview

Wildfires are strongly influenced by weather and environmental conditions. This project focuses on building an intelligent system that predicts the Fire Weather Index (FWI) using historical data and machine learning techniques.

The project covers the complete ML lifecycle — from data collection and preprocessing to model training, evaluation, and deployment using a Flask web application.

This project was developed as part of the Infosys Springboard Virtual Internship Program.

🎯 Objectives

To analyze weather and fire-related data affecting wildfire behavior

To build a reliable ML model for predicting Fire Weather Index (FWI)

To deploy the trained model as a user-friendly web application

To classify wildfire risk into Low, Moderate, High, and Extreme levels

🧠 Machine Learning Approach

Dataset: Algerian Forest Fire Dataset

Target Variable: Fire Weather Index (FWI)

Models Implemented:

Linear Regression

Ridge Regression ✅ (Final Model)

Lasso Regression

Random Forest Regression

Ridge Regression was selected for deployment due to its ability to handle multicollinearity and provide strong generalization performance.

⚙️ Features Used for Prediction

Temperature

Relative Humidity (RH)

Wind Speed (Ws)

Rain

FFMC

DMC

DC

ISI

BUI

📊 Model Performance (Ridge Regression)

R² Score: ~0.986

RMSE: ~0.74

MAE: ~0.55

The model shows high accuracy and consistent performance across validation tests.

🌐 Web Application (Flask)

The Flask-based web app allows users to:

Enter real-time environmental values

Get an instant FWI prediction

View a clear risk classification:

🔵 Low

🟡 Moderate

🟠 High

🔴 Extreme

The app follows the MVC architecture:

Model: ridge.pkl, scaler.pkl

Controller: app.py

View: HTML + CSS frontend

🛠️ Tech Stack

Programming Language: Python

Libraries:

pandas, numpy

matplotlib, seaborn

scikit-learn

Web Framework: Flask

Deployment Tools: Gunicorn

Frontend: HTML5, CSS3

🚀 How to Run the Project Locally

Clone the repository

git clone https://github.com/your-username/fwi-predictor.git


Navigate to the project folder

cd fwi-predictor


Install dependencies

pip install flask numpy


Run the Flask app

python app.py


Open your browser and go to

http://127.0.0.1:5000/

🔁 System Flow Chart

The following flow chart represents the end-to-end working of the Fire Weather Index Predictor, starting from user interaction to final risk classification.

This flow explains what happens before the Home page, during input processing, and at the result stage.

<img width="1024" height="1536" alt="final Flowchart" src="https://github.com/user-attachments/assets/ac7cb51e-277c-4ab3-babc-d336790c17d0" />

🧭 Application Page Flow

The application follows a simple and user-friendly navigation flow:

Home Page

Introduction to the Fire Weather Index Predictor

Button to start prediction
![HOMEPAGE](https://github.com/user-attachments/assets/663a256f-fec4-4fa9-a0be-8e8abf3736fa)

Input Page

User enters environmental and fire-related parameters

Form validation ensures correct inputs

![INPUT PAGE](https://github.com/user-attachments/assets/dbe2ea5b-450b-4eb2-ad82-fe0931ef6916)




# FIRE WEATHER INDEX PREDICTOR

## ABOUT FWI:

The Fire Weather Index (FWI) is used to understand the risk of forest fires based on weather conditions. 
It considers factors like temperature, humidity, wind speed, and rainfall to estimate how easily a fire can start and spread.
FWI helps in taking early precautions to reduce fire damage.

## PROBLEM STATEMENT:

Forest fires cause serious damage to forests, wildlife, and human life.
Predicting fire risk manually is difficult due to changing weather conditions.
There is a need for an automated system that can predict the Fire Weather Index (FWI) using environmental data.
This project aims to provide early fire risk prediction to support timely preventive actions.

## OBJECTIVES OF THE PROJECT:

1. To predict the Fire Weather Index (FWI) using machine learning.
2. To classify forest fire risk levels based on the predicted FWI.
3. To develop a user-friendly Flask web application for prediction

## PARAMETERS USED FOR PREDICTION:

The prediction is based on the following real-world parameters:

Temperature

Relative Humidity (RH)

Wind Speed

Rainfall

Fine Fuel Moisture Code (FFMC)

Duff Moisture Code (DMC)

Drought Code (DC)

Initial Spread Index (ISI)

Buildup Index (BUI)

These values are taken as input from the user and processed by the trained model.

## TOOLS AND TECHNOLOGIES:

1. python
 
2. Flask Web

3. Scikit-Learn

4. Numpy & Pandas 

5. HTML & CSS

## APPLICATION WORKFLOW:

<img width="1470" height="8191" alt="Start Decision Options Flow-2026-01-19-061747" src="https://github.com/user-attachments/assets/6b831397-91a4-421c-a224-e4313558b8c0" />

## WEB APPLICATION INTERFACE:
### HOME PAGE:

The home page allows the user to enter environmental and fuel-related parameters such as temperature, humidity, wind speed, rainfall, and fire indices. 
After entering the required values, the user can submit the form to predict the Fire Weather Index (FWI).

<img width="1807" height="872" alt="Screenshot 2026-01-22 152405" src="https://github.com/user-attachments/assets/7a7df571-714c-4fbf-835a-8dce33ea5d97" />

### OUTPUT PAGE:

The output page displays the predicted Fire Weather Index value based on the user inputs. 
It also shows the corresponding fire risk level and precautionary messages to help in early wildfire risk assessment.

<img width="1824" height="875" alt="Screenshot 2026-01-22 152433" src="https://github.com/user-attachments/assets/cf6fe5ee-55e5-4863-b7df-477709e8b8b0" />

## HOW TO CLONE THE PROJECT IN LOCALLY

Step 1: Clone the Repository:

```bash
git clone -b mounika https://github.com/Aspire-Infolabs/FWI_Prediction_Batch8.git
cd FWI_Project
```

Step 2: Create a Virtual Environment

```Bash
python -m venv venv
```
STEP 3:Activate the virtual environment:

Windows

```Bash
venv\Scripts\activate
```
macOS / Linux:

```Bash
source venv/bin/activate
```
Step 4: Install Required Dependencies:

```Bash
pip install -r requirements.txt
```

Step 5: Run the Flask Application

```Bash
python app.py
```
Step 6: Open the Application in Browser:

```bash
http://127.0.0.1:5000/
```

## CONCLUSION:

This project successfully demonstrates the application of machine learning techniques for predicting the Fire Weather Index based on environmental and fuel-related parameters. The integration of a trained model with a Flask-based web application enabled real-time prediction and clear visualization of fire risk levels. Through this project, practical experience was gained in data preprocessing, model deployment, and building user-friendly interfaces, highlighting the effective use of machine learning in wildfire risk assessment and prevention.

## AUTHOR

**NAME:** Mounika



# A Machine Learning System to Predict Fire Weather Index (FWI)

## Overview

Tempest: FWI Predictor is an end-to-end Machine Learning + Web Application designed to predict the Fire Weather Index (FWI) using environmental and meteorological parameters.
The system helps forest departments, disaster management teams, climate researchers, and planners to assess wildfire risk early and take preventive actions.
The project follows a modular internship-style workflow, covering:

Data collection & preprocessing
Exploratory data analysis (EDA)
Feature engineering & scaling
Model training & optimization
Model evaluation
Deployment via Flask with an interactive UI

## Why Fire Weather Index (FWI)?

FWI is a globally used indicator that measures fire danger based on:

Temperature
Relative Humidity
Wind Speed
Rainfall
Fuel moisture and dryness indicators
Higher FWI → Higher wildfire risk

## System Workflow

<img width="997" height="938" alt="image" src="https://github.com/user-attachments/assets/37307662-bddb-43f3-b52f-b1cce3d071bb" />

## Web interface of the application

### Home page(input page)

<img width="1881" height="913" alt="Screenshot 2026-01-21 201839" src="https://github.com/user-attachments/assets/0f5f5d43-828f-4cef-995c-f75464318076" />

### Result page 

<img width="1881" height="908" alt="Screenshot 2026-01-21 201915" src="https://github.com/user-attachments/assets/6c6464bf-042e-4224-83ee-f7e107e8b3d3" />


## Project Structure

FWI_Project/
│
├── data/
│   └── FWI Dataset.csv
│
├── notebooks/
│   └── FWI.ipynb
│
├── models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── FWI_app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       └── style.css
│
├── requirements.txt
├── README.md

## Dataset Description

The dataset contains real wildfire-related meteorological data.

Input Features
Temperature
Relative Humidity (RH)
Wind Speed (Ws)
Rain
FFMC
DMC
DC
ISI
BUI

## Target Variable

FWI (Fire Weather Index)

## Module-wise Implementation

### Module 1: Data Collection

Collected structured wildfire dataset
Loaded dataset using Pandas
Verified data types and consistency
Inspected dataset shape, columns, and samples

### Module 2: Data Exploration & Preprocessing

Missing value detection and handling
Outlier detection using boxplots and IQR
Histograms and density plots
Correlation matrix & heatmap
Scatter plots and pair plots
Label encoding for categorical features
Removed unnecessary columns
Saved cleaned dataset

### Module 3: Feature Engineering & Scaling

Selected features strongly correlated with FWI

Dropped irrelevant features
Applied StandardScaler for normalization
Split dataset into training and testing sets
Saved scaler as scaler.pkl

### Module 4: Model Training

Trained and compared 5 regression models:

Model	RMSE	R²
Linear Regression	~0.65	~0.99
Ridge Regression	~0.66	~0.99
Lasso Regression	~0.79	~0.98
Decision Tree	~1.41	~0.95
Random Forest	~0.82	~0.98

Ridge Regression selected due to:

High accuracy
Low error
Better generalization
Handles multicollinearity
Saved final model as ridge.pkl.

### Module 5: Evaluation & Optimization

### Evaluated using:
MAE
RMSE
R² Score

Applied GridSearchCV for hyperparameter tuning
Optimized alpha value
Compared Train vs Test performance

### Plotted:
Actual vs Predicted FWI
Residuals
Train vs Test accuracy

Confirmed no overfitting

### Module 6: Deployment (Flask App)

Built Flask backend (app.py)

Designed HTML templates:
index.html → user input
result.html → prediction output

Loaded ridge.pkl and scaler.pkl
Performed real-time prediction
Displayed FWI and risk category

## User Interface (UI)

Clean and user-friendly layout
Fire-themed design
Real-time prediction
Result visualization with charts

## How to Run the Project Locally

### Clone Repository
git clone https://github.com/your-username/FWI-Predictor.git
cd FWI-Predictor

### Install Dependencies
pip install -r requirements.txt

### Run Flask App
cd FWI_app
python app.py

### Open Browser
http://127.0.0.1:5000

## Tech Stack

Python
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
Flask
HTML, CSS

## Use Cases

Wildfire early warning systems
Climate risk analysis
Forest fire management
Academic & internship projects
ML + Flask deployment learning

## Conclusion

The Tempest: FWI Predictor project successfully demonstrates the design and implementation of a complete end-to-end machine learning system for predicting the Fire Weather Index (FWI) using real environmental and meteorological data.

Through systematic data collection, exploration, and preprocessing, meaningful features influencing wildfire risk were identified and prepared for modeling. Multiple machine learning algorithms were trained and evaluated, including Linear Regression, Ridge Regression, Lasso, Decision Tree, and Random Forest. Among these, Ridge Regression emerged as the most reliable model due to its strong predictive performance, low error values, and ability to handle multicollinearity effectively.

## Author

U P Mahendra
Bachelor of Engineering in Artificial Intelligence and Machine Learning
Project developed as part of SpringBoard Internship Program






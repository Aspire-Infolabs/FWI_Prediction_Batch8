 # Fire Weather Index (FWI) Prediction System

A Machine Learning–powered Fire Weather Index Predictor with a Flask-based web interface that estimates wildfire risk using environmental and meteorological parameters. This project delivers an end-to-end ML pipeline, from data preprocessing to real-time deployment, designed for early wildfire risk assessment.

## Overview

Wildfires pose a significant threat to ecosystems, human life, and property across the globe. Rising temperatures, changing climate patterns, and dry weather conditions have increased the frequency and intensity of forest fires in recent years. The Fire Weather Index (FWI) is a scientifically recognized metric used by meteorological and environmental agencies to estimate wildfire risk based on weather conditions and fuel moisture levels. This project presents an end-to-end Fire Weather Index Prediction System that applies machine learning techniques to predict FWI values accurately and make wildfire risk assessment accessible through a user-friendly web application.

## Problem Statement

Predicting wildfire risk at an early stage is crucial for disaster prevention and environmental protection. However, traditional wildfire assessment methods are often complex, time-consuming, and not easily accessible to the general public or field officers. There is a need for an automated, data-driven system that can analyze environmental conditions and instantly predict fire danger levels. This project addresses this challenge by developing a machine learning-based Fire Weather Index predictor and deploying it as a Flask web application, allowing users to input weather parameters and obtain real-time fire risk predictions.

## Project Objectives

The main objective of this project is to design and deploy a reliable machine learning model capable of predicting the Fire Weather Index using environmental data. The project aims to preprocess and clean real-world datasets, apply appropriate feature scaling techniques, train and evaluate multiple regression models, and select the best-performing model. Another key objective is to deploy the trained model using Flask to ensure the system is easy to use, interpretable, and accessible to non-technical users.

## Tech Stack
### Software & Libraries (with Versions)
| Layer | Technology | Version |
|------|-----------|--------|
| Language | Python | 3.11.8 |
| Data Processing | Pandas | 2.3.2 |
| Numerical Computing | NumPy | 1.26.4 |
| Visualization | Matplotlib | 3.10.7 |
| Visualization | Seaborn | 0.13.2 |
| Machine Learning | Scikit-learn | Latest |

## Dataset Description

**Source**: Kaggle – Algerian Forest Fires Dataset

**Target Variable**: FWI

**Input Features:**

| Feature Name | Description |
|-------------|------------|
| Temperature | Ambient temperature |
| RH | Relative humidity |
| Ws | Wind speed |
| Rain | Rainfall amount |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| DC | Drought Code |
| ISI | Initial Spread Index |
| BUI | Buildup Index |
| FWI | Fire Weather Index (Target) |

## Project WorkFlow

<p align="center">
  <img src="https://github.com/user-attachments/assets/e76213e7-4e71-4d15-bbe7-2aba62c5291b" width="500" />
</p>

### Data Collection

The workflow begins with collecting historical wildfire data from the Algerian Forest Fires dataset available on Kaggle. This dataset includes essential weather-related features such as temperature, humidity, wind speed, rainfall, and fire weather indices. The collected data serves as the foundation for training the machine learning model.

### Data Preprocessing

After data collection, the dataset is cleaned to improve quality and reliability. Missing values are handled appropriately, and outliers are removed using the Interquartile Range (IQR) method. Categorical features such as region are encoded into numerical format. The cleaned dataset is then saved for consistent use during model training.

### Feature Engineering and Scaling

Feature selection is performed by analyzing correlations between input variables and the Fire Weather Index. The most influential features are retained for modeling. To ensure all features contribute equally to the model, numerical values are standardized using the StandardScaler technique. This step improves model stability and performance.

### Model Training

Multiple regression models, including Linear Regression, Lasso Regression, Random Forest Regression, and Ridge Regression, are trained and evaluated. Ridge Regression is selected as the final model because it effectively handles multicollinearity and reduces overfitting. Hyperparameter tuning using GridSearchCV further enhances prediction accuracy.

### Model Evaluation and Optimization

The trained Ridge Regression model is evaluated using metrics such as R² score, Root Mean Squared Error (RMSE), and Mean Absolute Error (MAE). Actual versus predicted value plots are analyzed to verify consistency and accuracy across different fire risk levels. This evaluation ensures the model is reliable before deployment.

### Deployment and User Interaction

The final optimized model and scaler are deployed using a Flask web application. Users enter environmental parameters through an input form, and the application processes the data to predict the Fire Weather Index. The predicted FWI value is displayed along with a corresponding fire risk level—Low, Moderate, High, or Extreme—making the system easy to understand and use.

## How To Run The Project
### Step 1: Clone the Repository

Use Git to download the project source code to your local system.

```bash
git clone https://github.com/yourusername/fire-weather-index.git
cd fire-weather-index
```
### Step 2: Create a Virtual Environment

Create an isolated Python environment to manage dependencies cleanly.
 
```bash 
python -m venv venv
```
### Step 3: Activate the Virtual Environment

Activate the virtual environment based on your operating system.

```bash 
# Windows
venv\Scripts\activate
```
```bash 
# macOS / Linux
source venv/bin/activate
```
### Step 4: Install Required Dependencies

Install all necessary Python libraries listed in the requirements.txt file.

```bash 
pip install -r requirements.txt'
```
### Step 5: Run the Flask Application

Start the Flask development server.

```bash 
python app.py
```
### Step 6: Open the Application in Browser

Access the application using the local development URL.
```bash 
http://127.0.0.1:5000/
```
### Step 7: Use the Application

Enter the weather parameters such as temperature, humidity, wind speed, rainfall, and fire indices in the input form, then submit to view the predicted Fire Weather Index (FWI) and corresponding fire risk level.

## Expected Result

**Flask server runs successfully

**Web interface loads without errors

**Predicted FWI value is displayed

**Fire risk level shown as Low / Moderate / High / Extreme

## Conclusion

This project successfully demonstrates the application of machine learning for wildfire risk prediction. By combining effective data preprocessing, Ridge Regression modeling, and Flask-based deployment, the Fire Weather Index Prediction System provides an accurate, reliable, and user-friendly solution for early wildfire risk assessment. The system highlights how data-driven approaches can support environmental monitoring and disaster prevention efforts.


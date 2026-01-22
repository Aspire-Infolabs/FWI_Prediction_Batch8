 # Fire Weather Index (FWI) Prediction System

A Machine Learning–powered Fire Weather Index Predictor with a Flask-based web interface that estimates wildfire risk using environmental and meteorological parameters. This project delivers an end-to-end ML pipeline, from data preprocessing to real-time deployment, designed for early wildfire risk assessment.

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


## Web Application UI:
### index.html
Home page of the Fire Weather Index Prediction System displaying the project overview and key features

<p align="center">
  <img src="https://github.com/user-attachments/assets/5fa6b5e9-690b-47d3-8706-e620d0da9dc9" width="500" />
</p>

### home.html
User input interface of the Fire Weather Index Prediction System allowing users to enter weather parameters for real-time FWI prediction
<p align="center">
  <img src="https://github.com/user-attachments/assets/c05e15ce-5805-45ff-b59f-f40d2c0901e1" width="500" />
</p>

### Predicted FWI Result Page
Result page of the Fire Weather Index Prediction System displaying the predicted FWI value along with the corresponding fire risk level
<p align="center">
  <img src="https://github.com/user-attachments/assets/64b78c29-74eb-40b5-8d92-2e59c59a83ce" width="500" />
</p>

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

## Author

Mallisetti Meghana  
Developed as part of the Infosys Springboard Internship Program.  
Focused on building an end-to-end Fire Weather Index (FWI) prediction system using Machine Learning and Flask for real-time wildfire risk assessment.



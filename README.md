# 🔥 Fire Weather Index (FWI) Prediction – Flask Web Application

* This project is a Flask web application that uses machine learning to forecast the Fire Weather Index (FWI) based on meteorological data.
* The program runs on a local network and was created and tested in a Windows environment. 

# 1) Project Description:

* This project is a Flask web application that uses a machine learning model to forecast the Forest Fire Weather Index (FWI).
* The user enters weather-related values in a form, and the application calculates and displays the predicted FWI value. 
* This project runs on a local system and is developed for academic purposes.

# Environment:
* Operating System: Windows
* Python Version: Python 3.9 or above

# Technologies Used:
Python
Flask
NumPy
Pickle
HTML
CSS
Machine Learning (Ridge Regression)

# 2) System Requirements:

A)Hardware Requirements:
1.Minimum 4 GB RAM
2.Any standard laptop or desktop computer

B)Software Requirements:
1.Operating System: Windows, 
2.Python Version: Python 3.9 or above, 
3.Web Browser: Google Chrome / Microsoft Edge, 
4.Code Editor (optional): VS Code.

# 3) Steps to Run the FWI Flask Application:

Step 1: Open Command Prompt / PowerShell
```bash
cd path_to_project_folder
```

Step 2: Create Virtual Environment
 ```bash
 python -m venv venv
```
 
Step 3: Activate Virtual Environment
```bash
.\venv\Scripts\Activate.ps1
```

Step 4: Install Required Libraries
```bash
pip install -r requirements.txt
```

Step 5: Run the Application
```bash
python app.py
```

Step 6: Open Browser
```bash
http://127.0.0.1:5000/
```

# Output:

* The application displays the predicted Forest Fire Weather Index (FWI) based on the user-entered weather parameters.
* The predicted value is shown on the result page after successful submission of inputs.
* The application runs completely on the local system.


# 4) How the Application Works:
1.User enters fire weather parameters in the web form
2.Input values are scaled using scaler.pkl
3.Prediction is performed using the trained Ridge Regression model (ridge.pkl)
4.Predicted FWI value is displayed on the result page

## Web Application Screens:

### The web application consists of the following screens:

### 1. Home Page
* Displays the project title FWI Prediction
* Provides a brief description of the application
* Contains a button to start the prediction process

### 2. Prediction Page

## Displays an input form for entering fire weather parameters:
### Temperature
### Relative Humidity (RH)
### Wind Speed (WS)
### Rain
### FFMC
### DMC
### DC
### ISI
### BUI
* All input fields are mandatory
* Accepts only numeric values
* Includes a Predict FWI button

# Result Page
* Displays the predicted Fire Weather Index (FWI) value
* Shows a success message after prediction
* Provides a Go Back option to make another prediction

## How the Application Works:

* The user opens the web application in a browser.
* The user enters the required fire weather parameters in the input form.
* The submitted values are sent to the Flask backend.
* The input data is scaled using the saved scaler.pkl file.
* The scaled data is passed to the trained Ridge Regression model (ridge.pkl).
* The model predicts the Fire Weather Index (FWI).
* The predicted FWI value is displayed on the result page.

# 5) Conclusion:

* Using a Flask web application, this example effectively illustrates how to deploy a machine learning model.
* The system offers a useful method for estimating the Fire Weather Index by combining preprocessing, feature scaling, and Ridge Regression prediction.
* The tool is easy to use, effective, and appropriate for demonstration and academic settings.

# 6) Author: Manyatha N
## Academic Project – Forest Fire Weather Index (FWI) Prediction
## Developed as part of the Infosys Springboard Internship Program


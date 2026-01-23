## Fire Weather Index (FWI) Predictor :

A cutting-edge machine learning web application designed to predict the Fire Weather Index (FWI) using key meteorological and fire-danger parameters..Wildfires are becoming more frequent and dangerous due to climate change and extreme weather conditions, causing serious damage to forests, wildlife, and human life. An automated machine learning–based system is needed to provide fast and reliable fire risk predictions.


## Project Goal:
To create a fully functional Fire Weather Index prediction platform that:

1. Collects real-time environmental inputs 
2. Applies data preprocessing and feature scaling
3. Predicts FWI using a trained ML model
4. Classifies fire risk levels
5. Displays results in a user-friendly Flask web interface
6. Provides safety precautions and possible cause


## Workflow :  
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/6f1b2d8d-1d44-4e2c-8320-68a7f435ad9d" />


## Features Used for Prediction:

The model uses the following inputs:

1.Temperature	(°C)  
2.Relative Humidity (RH)(	%)  
3.Wind Speed	(km/h)  
4.Rainfall	(mm)  
5.FFMC	(Fine Fuel Moisture Code)  
6.DMC	(Duff Moisture Code)    
7.DC	(Drought Code)  
8.ISI	(Initial Spread Index)  
9.BUI	(Build-Up Index)  

The model uses the outputs is:

1.FWI


## System Requirements:

Hardware:  

•	Processor: Intel Core i3 or higher    
•	RAM: Minimum 4 GB (8 GB recommended)
•	Storage: Minimum 10 GB free disk space  

Software:  

•	Python 3.9+  
•	Flask   
•	Required Python libraries (requirements.txt)  

## Web Application Screenshots:        

•	Home Page:  
<img width="940" height="437" alt="image" src="https://github.com/user-attachments/assets/4c75f52d-e1a5-4f96-af0d-1fe8840aeda4" />

•	Result Page :  
<img width="940" height="432" alt="image" src="https://github.com/user-attachments/assets/687d970a-69b1-42e6-a474-d75945392629" /> 

•	Predict again page :  
<img width="1880" height="867" alt="image" src="https://github.com/user-attachments/assets/1c2da7a3-7446-4062-8dc0-2d279fc6e1c9" />


## Running the Project on Your Local Machine:  
Step 1: Clone the Project Repository:-  Start by copying the project files to your computer using Git.  
```
    git clone -b Dolly https://github.com/Aspire-Infolabs/FWI_Prediction_Batch8.git

    cd FWI_Prediction_Batch8
```
  
Step 2: Set Up a Virtual Environment:-
For Windows:
```
python -m venv venv

venv\Scripts\activate
```
For macOS / Linux:
```
python3 -m venv venv

source venv/bin/activate
```
This ensures all required packages are installed in an isolated environment.
  
Step 3: Install Dependencies:-
Install all the necessary Python libraries from the requirements file:
```
pip install -r requirements.txt
```
  
Step 4: Launch the Flask App:-
Start the web application with:
```
py app.py
```
Step 5: Open in Browser:-
Once the server starts, open your browser and go to:
```
http://127.0.0.1:5000
```
   
## Conclusion :  
  
This project demonstrates a complete pipeline for predicting the Fire Weather Index, from data processing and scaling to model training and deployment using Flask. The web application not only predicts FWI but also provides risk-level interpretation and safety guidance, making it a valuable tool for early wildfire warning and risk management enhance this with more words by examining this project whole and give conclusion.



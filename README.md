Fire Weather Index (FWI) Predictor :

A cutting-edge machine learning web application designed to predict the Fire Weather Index (FWI) using key meteorological and fire-danger parameters. This project was developed as part of the Infosys Springboard Virtual Internship Program.

Problem Overview:

Wildfires have become a growing threat to ecosystems, human life, and property worldwide. With climate change and extreme weather conditions, the frequency and intensity of forest fires have increased dramatically in recent years. These fires not only destroy forests but also lead to air pollution, loss of biodiversity, and significant economic damage. Therefore, effective wildfire prevention and management have become critical priorities for governments and environmental agencies.
The Fire Weather Index (FWI) is a widely recognized metric used to estimate the likelihood and severity of forest fires based on weather and fuel conditions. It combines multiple environmental factors such as temperature, humidity, wind speed, rainfall, and fuel moisture levels to calculate a single index value. This index helps meteorologists and disaster management teams evaluate fire risk and prepare proactive measures.
However, manually predicting the FWI using traditional methods can be time-consuming and prone to human error. Additionally, real-time weather changes and complex environmental interactions make accurate forecasting challenging. Therefore, there is a strong need for an automated system that can quickly process input data, generate accurate predictions, and present the results in a clear and actionable manner.

Objective:

The goal of this project is to build an end-to-end system that predicts the FWI using environmental data and provides actionable insights for wildfire prevention and management. By leveraging machine learning techniques, the system aims to enhance prediction accuracy, improve decision-making, and enable early warning for at-risk regions. This tool can assist forest departments, emergency responders, and policymakers in taking timely preventive measures, reducing the chances of wildfire disasters.
Project Goal:
To create a fully functional Fire Weather Index prediction platform that:
1. Collects real-time environmental inputs 
2. Applies data preprocessing and feature scaling
3. Predicts FWI using a trained ML model
4. Classifies fire risk levels
5. Displays results in a user-friendly Flask web interface
6. Provides safety precautions and possible cause
This system aims to support early warning, risk assessment, and proactive wildfire control strategies.

Key Deliverables:

Machine Learning Model
•	Built and trained a Ridge Regression model to predict FWI
•	Tested multiple regression algorithms and selected the best performer
•	Applied StandardScaler for accurate feature normalization
Web Deployment
•	Integrated the trained model into a Flask web application
•	Developed intuitive web pages for input and output
•	Displayed:
->	Predicted FWI value
-> Risk level classification
-> Causes and precautionary measures

Features Used for Prediction:

The model uses the following inputs:
Parameter	Description  
1.Temperature	(°C)  
2.Relative Humidity (RH)(	%)  
3.Wind Speed	(km/h)  
4.Rainfall	(mm)  
5.FFMC	(Fine Fuel Moisture Code)  
6.DMC	(Duff Moisture Code)    
7.DC	(Drought Code)  
8.ISI	(Initial Spread Index)  
9.BUI	(Build-Up Index)  

System Requirements:

Hardware  
•	Processor: Intel Core i3 or higher    
•	RAM: Minimum 4 GB (8 GB recommended)
•	Storage: Minimum 10 GB free disk space  
Software  
•	Python 3.9+  
•	Flask   
•	Required Python libraries (requirements.txt)  

 Web Application Screenshots:        
The application includes input and output pages such as:   
•	Home Page:
<img width="940" height="437" alt="image" src="https://github.com/user-attachments/assets/4c75f52d-e1a5-4f96-af0d-1fe8840aeda4" />
•	Result Page :
<img width="940" height="432" alt="image" src="https://github.com/user-attachments/assets/687d970a-69b1-42e6-a474-d75945392629" />    
•	Predict again page :
<img width="1880" height="867" alt="image" src="https://github.com/user-attachments/assets/1c2da7a3-7446-4062-8dc0-2d279fc6e1c9" />


Running the Project on Your Local Machine:  
Step 1: Clone the Project Repository:-  Start by copying the project files to your computer using Git.  
  
Step 2: Set Up a Virtual Environment:-
For Windows:
python -m venv venv
venv\Scripts\activate
For macOS / Linux:
python3 -m venv venv
source venv/bin/activate
This ensures all required packages are installed in an isolated environment.
  
Step 3: Install Dependencies:-
Install all the necessary Python libraries from the requirements file:
pip install -r requirements.txt
  
Step 4: Launch the Flask App:-
Start the web application with:
python app.py
  
Step 5: Open in Browser:-
Once the server starts, open your browser and go to:
http://127.0.0.1:5000
   
Conclusion :  
  
This project demonstrates a complete pipeline for predicting the Fire Weather Index, from data processing and scaling to model training and deployment using Flask. The web application not only predicts FWI but also provides risk-level interpretation and safety guidance, making it a valuable tool for early wildfire warning and risk management....... enhance this with more words by examining this project whole and give conclusion.



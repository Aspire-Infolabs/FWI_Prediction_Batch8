FWI Predictor – A Machine Learning Model to Predict Fire Weather Index  

Project Statement
Wildfires pose a significant threat to ecosystems, human life, and property. The Fire Weather Index (FWI) is a  crucial tool used by meteorological and environmental agencies worldwide to estimate wildfire potential. This  project aims to build a machine learning model that predicts FWI based on real-time environmental data, enabling  proactive wildfire risk management. The model is trained using Ridge Regression, deployed via a Flask web  application, and supports early warning systems for wildfire hazards. 

Outcomes:   
• A predictive ML model trained using Ridge Regression to forecast FWI.  
• A pre-processing pipeline using StandardScaler for normalization.  
• A Flask-based web app where users can input environmental values and get FWI predictions. 
• A system that can help forest departments, emergency planners, and climate researchers make data driven decisions.  

Modules to be implemented   
• Data Collection  
• Data Exploration (EDA) and Data Preprocessing  
• Feature Engineering and Scaling   
• Model Training using Ridge Regression  
• Evaluation and Optimization  
• Deployment via Flask App  
• Presentation and Documentation

Web Application (Flask) Features:
 - User-friendly form for entering weather and fire parameters
 - Backend preprocessing using saved scaler
 - Model inference using trained Ridge Regression model
 - Fire risk classification (Low, Moderate, High, Very High, Extreme)

Software
 - Operating System: Windows / Linux / macOS
 - Programming Language: Python 3.11 (or above)
 - Development Environment: VS Code with Jupyter Notebook extension
 - Web Browser: Google Chrome / Firefox / Microsoft Edge

Technologies Used
 - Python 3.11
 - Pandas, NumPy – Data handling
 - Matplotlib, Seaborn – Visualization
 - Scikit-learn – Model training & evaluation
 - Flask – Web application
 - Pickle – Model & scaler serialization

Run the Project

  1.Clone the repository
  
      git clone https://github.com/your-username/fwi-prediction-system.git
      cd fwi-prediction-system
      
  2.Create and activate a virtual environment

     - Windows

       python -m venv venv
       venv\Scripts\activate

     - macOS/Linux
     
       python3 -m venv venv
       source venv/bin/activate
      
  3.Install dependencies:
  
      pip install -r requirements.txt
      
  4.Run the Flask app:
  
      python app.py
      
  5.Open the browser and visit:
  
      http://127.0.0.1:5000/

Expected Outcome
 - Accurate prediction of Fire Weather Index values
 - Clear classification of fire risk levels
 - End-to-end ML pipeline deployment
 - Scalable foundation for future enhancements such as live weather APIs and cloud deployment

Project Status
 - Model training and optimization completed
 - Evaluation and visualization approved
 - Flask deployment functional
 - Documentation and reproducibility ensured

WORKFLOW

<img width="271" height="941" alt="fwi drawio" src="https://github.com/user-attachments/assets/2e7c7f02-8d13-4092-8f01-62ac3930a63b" />

Input Features
 - Temperature – Ambient air temperature
 - RH – Relative Humidity
 - Ws – Wind Speed
 - Rain – Rainfall
 - FFMC – Fine Fuel Moisture Code
 - DMC – Duff Moisture Code
 - DC – Drought Code
 - ISI – Initial Spread Index
 - BUI – Buildup Index

Target Variable
  FWI (Fire Weather Index)
 
WEBPAGE

<img width="1286" height="929" alt="Screenshot 2026-01-18 224546" src="https://github.com/user-attachments/assets/ad74eea3-8a63-45ad-b70b-bc79943c92a1" />
<img width="907" height="260" alt="Screenshot 2026-01-18 224818" src="https://github.com/user-attachments/assets/9bd56cfe-7b5d-4ee6-96a6-fdbbbb178cdc" />
<img width="821" height="265" alt="Screenshot 2026-01-18 225029" src="https://github.com/user-attachments/assets/4655edc7-6500-49bf-bf8d-996196c8c254" />


Future Scope
 - Integration with real-time weather APIs
 - Cloud deployment (AWS / Azure)
 - Mobile-friendly interface
 - Alert-based fire warning system

Conclusion
  This project successfully demonstrates an end-to-end machine learning pipeline for predicting the Fire Weather Index (FWI) using meteorological data. By integrating a trained and optimized Ridge Regression model into a Flask web application, the system enables real-time fire risk prediction with clear risk classification. The project highlights practical skills in data preprocessing, model evaluation, deployment, and reproducibility.

Author
 Srinanda C S
 Infosys Springboard Internship Project

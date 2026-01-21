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

Technologies Used
 - Python 3.11
 - Pandas, NumPy – Data handling
 - Matplotlib, Seaborn – Visualization
 - Scikit-learn – Model training & evaluation
 - Flask – Web application
 - Pickle – Model & scaler serialization

Run the Project
  1.Clone the repository
  2.Create and activate a virtual environment
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

Future Scope
 - Integration with real-time weather APIs
 - Cloud deployment (AWS / Azure)
 - Mobile-friendly interface
 - Alert-based fire warning system


Author
Srinanda C S
Infosys Springboard Internship Project

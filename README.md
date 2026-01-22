**Fire Weather Index (FWI) Prediction System**

**Project Overview**

The Fire Weather Index (FWI) Prediction System is a machine learning–based application developed as part of the Infosys Springboard Virtual Internship Program.
The project predicts the Fire Weather Index (FWI) using environmental and meteorological parameters such as temperature, humidity, wind speed, rainfall, and fire weather components.

The system follows a complete end-to-end machine learning pipeline, starting from data preprocessing and model training to deployment as a Flask web application.

**Problem Statement**

Wildfires pose serious threats to ecosystems, property, and human life. The Fire Weather Index (FWI) is a widely used indicator to estimate wildfire risk based on weather and environmental conditions.
This project aims to build a predictive model that can estimate the FWI value and classify fire risk levels to assist in early risk assessment and decision-making.

**Project Structure**
<img width="7931" height="1255" alt="Project Structure" src="https://github.com/user-attachments/assets/1d1dc449-3988-4df5-a87e-83bc02a483dd" />



**System Architecture & Workflow
System Architecture Diagram**

<img width="4487" height="1837" alt="SystemArchitecture" src="https://github.com/user-attachments/assets/d00190c0-521a-4273-9e0e-6353af8cba2d" />


System Workflow Diagram

<img width="1240" height="4050" alt="Workflow" src="https://github.com/user-attachments/assets/7b59fbfc-eb92-4642-a0b4-4ed5044e2f73" />




**Technologies Used**

- Python 3.9+

- Pandas
  
- NumPy
  
- Matplotlib
  
- Seaborn
  
- Scikit-learn
  
- Flask
  
- HTML & CSS

**Dependencies Installation**

All required dependencies are listed in requirements.txt.

**Install dependencies (All OS)**

_pip install -r requirements.txt_

**How to Run the Project**

**Step 1:** Clone the Repository
git clone <your-repository-url>
cd FWI-Predictor

**Step 2:** Verify Dataset Location

Ensure the dataset is present in:

_Datasets/FWI Dataset.csv_

**Step 3:** Run the Jupyter Notebook (Model Training)

Open and run the notebook:

_FWI Dataset.ipynb_


**This notebook covers:**

- Data preprocessing
  
- Feature engineering
  
- Scaling
  
- Model training
  
- Evaluation
  
- Saving ridge.pkl and scaler.pkl



**Step 4:** Verify Model Files

Ensure the following files exist after notebook execution:

Models

**ridge.pkl and scaler.pkl**


**Step 5:** Run Flask Application

From the project root directory, run:

_python app.py_


You should see:

_Running on http://127.0.0.1:5000/_

**Step 6:** Access Web Application

Open your browser and go to:

_http://127.0.0.1:5000_


<img width="1360" height="720" alt="Screenshot (137)" src="https://github.com/user-attachments/assets/ee4a943b-7b91-4f94-9337-79492ead74a1" />


**Step 7:** Enter Inputs & Predict

Enter environmental parameters

Submit the form

View predicted FWI value and Fire Risk Category

<img width="1360" height="721" alt="Screenshot (138)" src="https://github.com/user-attachments/assets/6da0c7e4-9d22-4a30-8589-8939c6bbe65e" />



<img width="1360" height="721" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/f0e146c9-b9e9-4d4c-a216-af8ba8ff4ab7" />


### Fire Weather Index (FWI) Risk Classification

| FWI Range   | Risk Level |
|-------------|------------|
| < 5.2       | Very Low   |
| 5.2 – 11.2  | Low        |
| 11.2 – 21.3 | Moderate   |
| 21.3 – 38.0 | High       |
| 38.0 – 50   | Very High  |
| > 50        | Extreme    |


**Running on Different Operating Systems**
**Windows**

_python app.py_

**macOS / Linux**

_python3 app.py_


**Ensure Python is installed:**

_python --version_


**Key Features**

1. End-to-end ML pipeline

2. Feature scaling consistency using saved scaler

3. Ridge Regression to handle multicollinearity

4. Clean and intuitive web interface

5. Real-time FWI prediction

6. Risk category interpretation

**Future Enhancements**

- Integration with live weather APIs

- Advanced ML models (Random Forest, XGBoost)

- Cloud deployment

- Mobile-friendly interface

- Automated data updates

**Conclusion**

This project demonstrates the practical application of machine learning in environmental risk assessment. It provides a complete workflow from data analysis to deployment, making it suitable for academic learning, research reference, and real-world applications.

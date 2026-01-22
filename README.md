# 🔥 Fire Weather Index (FWI) Predictor

A **Machine Learning–based web application** to predict **Fire Weather Index (FWI)** using environmental and fire-danger parameters.  
Developed as part of the **Infosys Springboard Virtual Internship Program**.

---

##  Problem Statement

Wildfires pose a serious threat to **ecosystems, human life, and property**.  
The **Fire Weather Index (FWI)** is a globally used indicator to estimate forest fire danger based on **weather conditions and fuel moisture content**.

This project aims to develop an **end-to-end Fire Weather Index prediction system** using Machine Learning.  
The system:
- Processes key meteorological and fire-related parameters
- Predicts the **FWI value**
- Classifies **fire risk levels**
- Displays results using a **Flask web application**

 **Goal:** Support early warning, risk assessment, and informed decision-making for wildfire management.

---

##  Project Outcomes

-  Trained a **Ridge Regression** model to predict Fire Weather Index  
-  Applied **StandardScaler** for feature normalization  
-  Evaluated multiple regression models and selected the best performer  
-  Deployed the trained model using a **Flask web application**  
-  Displayed predicted FWI value along with **fire risk level, causes, and precautions**

---

##  Features Used

- Temperature  
- Relative Humidity (RH)  
- Wind Speed  
- Rainfall  
- FFMC (Fine Fuel Moisture Code)  
- DMC (Duff Moisture Code)  
- DC (Drought Code)  
- ISI (Initial Spread Index)  
- BUI (Build-Up Index)  

---

##  System Requirements

###  Hardware
- **Processor:** Intel Core i3 or higher  
- **RAM:** Minimum 4 GB (8 GB recommended)  
- **Storage:** At least 10 GB free disk space  

###  Software
- **Python:** 3.9 or above  
- **Flask**  
- Required Python libraries (see `requirements.txt`)  

---

##  Web Application Screens

### 1️ User Signup Page
<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/4fad324c-a447-4638-8773-889cd8d12cec">
</p>

---

### 2️ User Login Page
<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/836b3176-1400-4602-8cd4-b799e3f1a7d1">
</p>

---

### 3️ Home Page
<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/43bc96a5-e9f5-4139-8e6d-41d449a22465">
</p>

---

### 4️ FWI Prediction Input Page
<p align="center">
  <img width="700" src="https://github.com/user-attachments/assets/3e80f4c0-ceb0-473c-bb62-5a61587f3922">
</p>

---

### 5️ Prediction Result Page
<p align="center">
  <img width="600" src="https://github.com/user-attachments/assets/79dda3e0-8fd1-4030-99b4-36c3e442a6af">
</p>

---

##  Workflow Diagram

<p align="center">
  <img width="900" src="https://github.com/user-attachments/assets/12273a80-79e2-44cd-a96b-a249c5b8b7d3">
</p>

---

##  Steps to Run the FWI Flask App

### 1️ Clone the Repository
git clone https://github.com/Aspire-Infolabs/FWI_Prediction_Batch8.git
cd FWI_Prediction_Batch8
### 2 Create a Virtual Environment
python -m venv .venv
### 3.Windows (PowerShell):
.venv\Scripts\activate
### 4.Install Required Dependencies
pip install -r requirements.txt
### This installs:
Flask

pandas

numpy

scikit-learn

scipy

matplotlib

seaborn

openpyxl
5.Run the Flask Application
python app.py
### Conclusion:-This project demonstrates how Machine Learning + Flask can be effectively used
to build a real-world wildfire prediction system for early warning and prevention.



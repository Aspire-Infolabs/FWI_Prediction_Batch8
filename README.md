# 🔥 Fire Weather Index (FWI) Predictor

<p align="center">
A Machine Learning–based web application to predict Fire Weather Index (FWI)  
using environmental and meteorological parameters.
</p>

---

## 📌 Project Overview

Fire Weather Index (FWI) Predictor is an intelligent machine learning–based web application  
designed to **predict wildfire risk** using weather and fuel conditions.

It helps in:
- 🌲 Early detection of forest fire risks  
- ⚠️ Risk assessment & prevention  
- 🧠 Decision-making for wildfire management  

---

## ❓ Why FWI Prediction?

Forest fires cause massive damage to:
- Ecosystems 🌱  
- Wildlife 🐾  
- Human life & property 🏠  

Predicting fire risk **in advance** enables authorities to take **preventive actions**.

---

## ⭐ Key Features

- ✔️ Machine Learning–based FWI prediction  
- ✔️ Fire risk classification (Low / Moderate / High / Extreme)  
- ✔️ Secure user **Login & Signup**  
- ✔️ User-friendly web interface  
- ✔️ Region-wise fire risk prediction  

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Machine Learning**
- **Scikit-learn**
- **HTML**
- **CSS**

---

## 👩‍💻 Project Details

- **Prepared By:** Tarigopula Sri Kavya  
- **Mentor:** Praveen  
- **Internship:** SpringBoard Internship Project  

---

## 🖥️ Web Application Screens

### 🔐 User Signup Page
<p align="center">
  <img src="images/signup.png" width="400">
</p>

---

### 🔑 User Login Page
<p align="center">
  <img src="images/login.png" width="400">
</p>

---

### 🏠 Home Page
<p align="center">
  <img src="images/home.png" width="400">
</p>

---

### 🔥 FWI Prediction Input Page
<p align="center">
  <img src="images/predict_input.png" width="400">
</p>

---

### 📊 Prediction Result Page
<p align="center">
  <img src="images/result.png" width="400">
</p>

---

## 📊 Model Information

- Algorithm Used: **Ridge Regression**
- Feature Scaling: **StandardScaler**
- Target Variable: **Fire Weather Index (FWI)**

---

## 💻 System Requirements

- **Processor:** Intel Core i3 or higher  
- **RAM:** Minimum 4 GB  
- **Storage:** At least 10 GB free space  

---

## 🧪 How to Run the Project

```bash
# Clone repository
git clone https://github.com/Aspire-Infolabs/FWI_Prediction_Batch8.git

# Navigate to project folder
cd FWI_Flask_App

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Train model (if needed)
python save_model.py

# Run application
python app.py

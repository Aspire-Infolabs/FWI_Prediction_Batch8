**Fire Weather Index (FWI) Prediction System**

The Fire Weather Index (FWI) Prediction System is a machine learning–based web application that predicts the Fire Weather Index, 
which indicates the risk of forest fire occurrence based on weather and environmental conditions.
This project helps users understand whether the current weather conditions indicate a Low, Moderate, High, or Extreme fire risk.


**PROJECT OBJECTIVE**

**.** To learn how real-world environmental data is used

**.** To apply machine learning for prediction

**.** To convert a trained ML model into a working web application

**.** To make fire risk prediction simple and understandable

**Technologies Used**

**Programming & Libraries**

-Python 

-Pandas & NumPy

-Scikit-learn

-Matplotlib & Seaborn

**Web Technologies**
-Flask (Backend)

-HTML & CSS (Frontend)

**Tools**

-VS Code

-Jupyter Notebook


<img width="436" height="761" alt="image" src="https://github.com/user-attachments/assets/df45b854-778b-43a3-9f44-93f101d3f7ce" />


**Model Used: Ridge Regression**

Ridge Regression helps control overfitting and works well with correlated features.

Scaling: StandardScaler

Evaluation: MAE, RMSE, R² Score

Hyperparameter Used: Alpha (regularization strength)

**Inputs parameters for Prediction**

The user enters the following values:

Temperature

Relative Humidity (RH)

Wind Speed (Ws)

Rain

FFMC

DMC

DC

ISI

BUI

****How to Run the Project****

Step 1: Clone the Repository

git clone <your-repo-link>
cd FWI_predictor

Step 2: Create and Activate Virtual Environment

python -m venv myenv

myenv\Scripts\activate

Step 3: Install Required Packages

pip install -r requirements.txt

Step 4: Run the Flask App

python app.py

Step 5: Open Browser
http://127.0.0.1:5000

**SCREENSHOTS WEB APPLICATION:**

index.html

<img width="1918" height="938" alt="indexpage" src="https://github.com/user-attachments/assets/0a666cdd-1a9a-4617-8808-12efb1590aca" />

output.html

<img width="1915" height="967" alt="image" src="https://github.com/user-attachments/assets/1a05eab9-2ea4-4bf1-849e-45f3ce3433f3" />


**CONCLUSION**

This project helped me understand:

-How data affects forest fire risk

-How machine learning models are built and evaluated

-How to deploy a model as a web application

It is a beginner-friendly machine learning project that connects theory with real-world application.

Author: Devinandhana (as part infosys virtual internship)

🔥 Fire Weather Index (FWI) Predictor

A Machine Learning–based web application that predicts the Fire Weather Index (FWI) using environmental and fire-danger parameters. The system helps assess wildfire risk levels and supports early warning and decision-making for forest fire management.



📌 Project Statement

Wildfires are strongly influenced by weather and environmental conditions. This project focuses on building an intelligent system that predicts the Fire Weather Index (FWI) using historical data and machine learning techniques.The project covers the complete ML lifecycle — from data collection and preprocessing to model training, evaluation, and deployment using a Flask web application.This project was developed as part of the Infosys Springboard Virtual Internship Program.



🎯 Problem Outcomes

a.Analysed weather and fire-related data affecting wildfire behavior.

b.Build a reliable ML model for predicting Fire Weather Index (FWI).

c.Deployed the trained model as a user-friendly web application.

d.Classified wildfire risk into Low, Moderate, High, and Extreme levels.



⚙️ Features Used 

Temperature

Relative Humidity (RH)

Wind Speed (Ws)

Rain

FFMC

DMC

DC

ISI

BUI



🌐 Web Application (Flask)

The Flask-based web app allows users to:

a.Enter real-time environmental values.

b.Get an instant FWI prediction.

c.View a clear risk classification.

🔵 Low

🟡 Moderate

🟠 High

🔴 Extreme



🛠️ Tech Stack

Programming Language: Python

Libraries:pandas, numpymatplotlib, seabornscikit-learn

Web Framework: Flask

Deployment Tools: Gunicorn

Frontend: HTML5, CSS3



🚀 How to Run the Project Locally

1.Clone the repository
git clone https://github.com/your-username/fwi-predictor.git

2.Navigate to the project folder

cd fwi-predictor

3.Install dependencies

pip install flask numpy

4.Run the Flask app

python app.py

5.Open your browser and go to

http://127.0.0.1:5000/



🔁 System Flow Chart

The following flow chart represents the end-to-end working of the Fire Weather Index Predictor, starting from user interaction to final risk classification.
This flow explains what happens before the Home page, during input processing, and at the result stage.

<img width="1024" height="1536" alt="final Flowchart" src="https://github.com/user-attachments/assets/ac7cb51e-277c-4ab3-babc-d336790c17d0" />


🧭 Application Page Flow

The application follows a simple and user-friendly navigation flow:

Home Page

a.Introduction to the Fire Weather Index Predictor.

b.Button to start prediction.

![HOMEPAGE](https://github.com/user-attachments/assets/663a256f-fec4-4fa9-a0be-8e8abf3736fa)


Input Page

a.User enters environmental and fire-related parameters.

b.Form validation ensures correct inputs.

![INPUT PAGE](https://github.com/user-attachments/assets/dbe2ea5b-450b-4eb2-ad82-fe0931ef6916)

Result Page

a.Displays predicted FWI value.

b.Shows risk category (Low / Moderate / High / Extreme).

c.Provides clear visual feedback for decision-making.

HIGH FWI VALUE


![A22](https://github.com/user-attachments/assets/7111a807-cf0e-4ca2-9a90-3884fbb28c82)

MODERATE FWI VALUE


![A44](https://github.com/user-attachments/assets/a52fe1cd-0b27-492b-90cc-d85d1c57f4fb)

EXTREME FWI VALUE


![A66](https://github.com/user-attachments/assets/288c4c84-25db-4447-8b81-492807b3cef8)



✅ Conclusion

This project successfully demonstrates the complete development and deployment of a Fire Weather Index (FWI) Prediction System using machine learning. By analyzing key environmental and fire-related parameters such as temperature, humidity, wind speed, rainfall, and fire danger indices, the system is able to accurately predict the Fire Weather Index and classify wildfire risk levels.Overall, this project provides a practical and user-friendly solution for wildfire risk assessment. It can assist forest departments, disaster management authorities, researchers, and environmental planners in early detection, preparedness, and informed decision-making. With further enhancements such as real-time data integration and advanced models, the system can be extended into a powerful tool for wildfire monitoring and prevention.












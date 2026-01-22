# Fire Weather Index (FWI) Predictor
Wildfires can spread quickly and cause heavy damage, so it is important to know the fire risk 
in advance. The Fire Weather Index (FWI) helps measure how likely a fire is to start, but 
calculating it manually is not always accurate or fast. To solve this, the aim of this project is 
to use environmental factors like temperature, humidity, wind speed, and rainfall to build a 
machine learning model that can predict the FWI automatically. This will help in giving early 
warnings and improving wildfire preparedness.

### Objectives
• To study the weather factors that affect the Fire Weather Index (FWI).<br>
• To clean and prepare the dataset for accurate analysis.<br> 
• To explore the data and understand its patterns.<br> 
• To build a machine learning model that can predict FWI.<br> 
• To test the model and improve its accuracy.<br> 
• To create a simple web app for making FWI predictions.<br>

### Input Features
• ISI<br> 
• DMC<br> 
• BUI<br> 
• DC<br> 
• FFMC<br>
• Temperature<br>
• Rain<br>
• RH<br>
• Ws<br>

### Output Feature
• FWI

### Software Required
Python 3.9 or above<br>
Code Editor: Visual Studio Code With Jupyter Notebook Extension(Recommended)<br>
Web Browser: Google Chrome(Recommended)<br>
Python Libraries(Check requirements.txt)

### How to run the project locally
Step 1: Clone the repository
```
 git clone -b Pranjali https://github.com/Aspire-Infolabs/FWI_Prediction_Batch8.git
 cd FWI_Prediction_Batch8
```

Step 2: Create a Virtual Environment<br>
&nbsp;&nbsp; • Windows
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
&nbsp;&nbsp; • macOS / Linux
  ```
  python -m venv venv
  source venv/bin/activate
  ```

Step 3: Install Required Libraries
```
pip install -r requirements.txt
```

Step 4: Run the Flask Application
```
python app.py
```

Step 5: Open in Browser
```
http://127.0.0.1:5000/
```

### Results
##### Home Page<br>
<img width="900" height="550" alt="image" src="https://github.com/user-attachments/assets/2160b752-4f0b-494b-a400-d8e950b825fe" />

##### About Page<br>
<img width="900" height="550" alt="image" src="https://github.com/user-attachments/assets/48077992-40f1-4caf-8c4e-0dd7befce112" />

##### Predictor Page<br>
<img width="900" height="550" alt="image" src="https://github.com/user-attachments/assets/624a0d9c-261a-4a7a-8ff4-1322eec107d7" />

### Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow, from data preprocessing 
and model training to deployment using a Flask web application. It helped in understanding how real-world 
environmental data can be used to predict the Fire Weather Index (FWI) and how ML models can be integrated 
into practical applications. This project serves as a strong learning experience for beginners and provides 
a foundation for building real-time predictive systems.










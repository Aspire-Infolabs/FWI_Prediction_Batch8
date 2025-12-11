This repository contains a machine learning model built using scikit-learn to predict the Fire Weather Index (FWI) based on various meteorological and environmental factors. The dataset includes columns such as day, month, year, temperature, relative humidity (RH), wind speed (WS), rain, and several indices (FFMC, DMC, DC, ISI, BUI). The model aims to predict the FWI, which is crucial for wildfire risk assessment.

Dataset
The dataset contains the following columns:

Day: Day of the observation.
Month: Month of the observation.
Year: Year of the observation.
Temperature: Temperature in Celsius.
RH: Relative Humidity (%) - The percentage of moisture in the air.
Ws: Wind Speed (km/h).
Rain: Rainfall (mm).
FFMC: Fine Fuel Moisture Code - Represents moisture content in fine fuels.
DMC: Duff Moisture Code - Represents moisture in the duff (organic material on the forest floor).
DC: Drought Code - Indicates long-term drying trends in the forest.
ISI: Initial Spread Index - Reflects the rate of fire spread in fine fuels.
BUI: Build Up Index - Reflects the amount of fuel available for combustion.
FWI: Fire Weather Index - The target variable for the prediction model.
Classes: Class label (Feu ou Pas Feu) indicating if a fire occurred or not.
Region:Bejaia and Sidi-Bel Abbes.

Objective
The goal is to create a machine learning model using scikit-learn that predicts the FWI based on the features from the dataset. The FWI is a crucial metric used to evaluate fire risk, and predicting it accurately can aid in fire prevention and response strategies.

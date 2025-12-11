Fire Weather Index (FWI) Prediction – Infosys Springboard Internship

Milestone 1 – Data Collection, Exploration & Preprocessing

1. Project Overview

This project is part of the Infosys Springboard Virtual Internship Program, where the objective is to understand and develop a predictive system for the Fire Weather Index (FWI) using real environmental and meteorological parameters. FWI is a globally recognized indicator used to estimate the likelihood and severity of forest fires.

Through the internship, we aim to build a complete machine learning solution — from dataset collection and preprocessing to FWI prediction and deployment using a Flask application.

2. Problem Statement

Wildfires have become increasingly hazardous to ecosystems, human settlements, and national environmental security. Predicting fire danger levels in advance can help authorities take preventive actions and allocate resources efficiently.

The challenge is to:

Analyze meteorological features such as temperature, humidity, rainfall, and wind speed

Study fire-related indices like FFMC, DMC, DC, ISI, and FWI

Build a modeling approach capable of predicting FWI accurately

Prepare the dataset through systematic preprocessing

This Milestone focuses on preparing clean, reliable data suitable for modeling.

3. Project Objectives

The core objectives for Milestone 1 were:

Module 1 – Data Collection

Load the dataset into a Pandas DataFrame

Understand data structure, formats, and types

Verify availability of required environmental and fire index variables

Perform initial inspection using head(), info(), describe()

Check for formatting issues, inconsistent values, or missing entries

Module 2 – Data Exploration & Preprocessing

Identify and handle missing values using mode and mean imputation

Clean inconsistencies in numeric fields (DC, FWI)

Remove unnecessary whitespace from categorical columns

Perform exploratory analysis (histograms, boxplots, scatterplots)

Generate a correlation matrix to explore feature relationships

Encode categorical variables such as Region for modeling


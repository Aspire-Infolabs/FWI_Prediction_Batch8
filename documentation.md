# Fire Weather Index Prediction 
# Milestone 1 Documentation

## Week 1–2 — Module 1 & Module 2

---

## Module 1: Data Collection
- Collected structured dataset containing environmental attributes and the FWI target value.
- Dataset features include:
  - Temperature
  - Relative Humidity
  - Wind Speed
  - Rain
  - FFMC
  - DMC
  - ISI
  - Region
- Verified datatype consistency and resolved formatting issues.
- Loaded dataset into Pandas DataFrame for further analysis.
- Conducted initial inspection using:
  - df.info()
  - df.describe()
  - Shape and head preview

---

## Module 2: Data Exploration & Preprocessing
- Checked for missing / null values using df.isnull().sum().
- Performed outlier detection using:
  - Boxplots
  - Statistical thresholds (IQR method)
- Analyzed feature distributions via:
  - Histograms
  - Density plots
- Explored feature relationships:
  - Correlation matrix
  - Scatterplots
- Encoded categorical attribute Region using **One-Hot Encoding**.
- Final cleaned dataset saved into /data/cleaned/ folder.

---



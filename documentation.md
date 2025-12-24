# Fire Weather Index Prediction 
# Milestone 1 Documentation

## Week 1–2 — Module 1 & Module 2

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

Week 3–4 — Module 3 & Module 4

Milestone 2: This milestone focuses on preparing the dataset for machine learning and training a regression model to predict the Fire Weather Index (FWI).

## Module 3: Feature Engineering and Scaling

-Selected important input features based on correlation with FWI target variable.
-Removed irrelevant and weakly correlated features to improve model efficiency.
-Split the dataset into:
        Input features (X)
        Target variable (y – FWI)
-Divided data into training and testing sets using train_test_split.
-Applied StandardScaler to normalize numerical features for consistent scaling.
-Fitted the scaler only on training data to avoid data leakage.
-Saved the trained scaler as scaler.pkl for deployment consistency.

## Module 4: Model Training Using Ridge Regression

-Selected Ridge Regression to handle multicollinearity in meteorological features.
-Trained the Ridge model on scaled training data.
-Tuned the alpha (regularization strength) parameter to balance bias–variance trade-off.
-Evaluated model performance using:
-R² Score
-Mean Squared Error (MSE)
-Compared training and testing performance to detect overfitting.
-Saved the trained model as ridge.pkl for future inference and deployment.



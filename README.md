Fire Weather Index (FWI) Prediction Project  
Module 1 and Module 2  

Submitted By: U P Mahendra  
Domain: Machine Learning  
Dataset: Fire Weather Index (FWI) Dataset – Kaggle  
Programming Language: Python  

PROJECT PURPOSE

The purpose of this project is to build a machine learning system to predict the Fire Weather Index (FWI) using environmental and weather data.  
Module 1 and Module 2 focus completely on preparing high-quality data for accurate model training.

MODULE 1: DATA COLLECTION AND INITIAL DATA INSPECTION

Objective:
To load the dataset, clean the data structure, verify data types, and identify missing values before preprocessing.

Work Done in Module 1:
1. Loaded the dataset using Pandas.
2. Cleaned column names by removing extra spaces.
3. Converted DC and FWI columns into numeric values.
4. Converted Region values from numeric form to readable text.
5. Displayed random sample records from the dataset.
6. Identified rows that contain missing values.
7. Displayed full dataset structure using df.info().
8. Displayed column-wise missing value count.

Main Outputs from Module 1:
- Random dataset records.
- Rows with missing values.
- Dataset size, column names, and data types.
- Missing value count in each column.

Result of Module 1:
The dataset was successfully loaded, cleaned at the column level, and inspected. All missing values and incorrect data types were clearly identified for further processing.

MODULE 2: DATA EXPLORATION AND DATA PREPROCESSING

Objective:
To clean the dataset completely, remove inconsistencies, analyze data behavior, and prepare a final dataset for machine learning.

Work Done in Module 2:

Missing Value Handling:
- Filled missing values in the Classes column using forward fill.
- Filled missing values in numeric columns using mean imputation.
- After this step, the dataset contained no missing values.

Outlier Detection:
- Applied the IQR (Interquartile Range) method.
- Detected outliers in Temperature, Wind Speed, Rain, FFMC, DMC, DC, ISI, BUI, and FWI.
- Used boxplots for visual confirmation.

Data Visualization:
- Generated histograms for all major numerical features.
- Applied log transformation to reduce skewness.
- Created correlation heatmap.
- Created scatter plots and pair plots.

Correlation Analysis:
- Found strong positive correlation between FWI and ISI, DMC, BUI, and DC.
- Found negative correlation between FWI and Rain and RH.

Categorical Data Encoding:
- Applied Label Encoding to the Region column.

Column Removal:
- Removed the Classes column to prevent data leakage.

Final Data Type Conversion:
- Converted FWI and DC into int64.

Final Dataset Saving:
- Saved the cleaned dataset as:
  FWI_Dataset_Final.csv

FINAL OUTPUT AFTER MODULE 2

- No missing values in the dataset.
- All important features cleaned and verified.
- Region column encoded numerically.
- Classes column completely removed.
- FWI and DC converted to integer format.
- Final dataset ready for feature engineering and model training.

FINAL CONCLUSION

Module 1 and Module 2 completed the entire data loading, inspection, cleaning, visualization, and preprocessing process.  
The dataset is now fully prepared for machine learning model development with improved accuracy and reliability.


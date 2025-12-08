import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/cleaned_fwi.csv")

print("Dataset loaded successfully!\n")
print(df.head())
print("\nMissing values after cleaning:\n")
print(df.isnull().sum())

# histogram
df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()

# Boxplots for detecting outliers
plt.figure(figsize=(12, 8))
df.boxplot()
plt.xticks(rotation=45)
plt.show()

# Remove outliers using IQR method
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("\nAfter removing outliers, dataset shape:", df.shape)

if df['Region'].dtype == 'object':
    le = LabelEncoder()
    df['Region'] = le.fit_transform(df['Region'])

print("\nRegion column encoded successfully!")
print(df['Region'].head())

df.to_csv("data/cleaned_fwi.csv", index=False)
print("\nSaved: data/cleaned_fwi.csv")
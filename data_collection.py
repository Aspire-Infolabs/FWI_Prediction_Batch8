import pandas as pd

df = pd.read_csv("data/FWI_Dataset.csv")

print(df.head())
print(df.info())
print(df.describe())

df.columns = df.columns.str.strip()

print("Missing values before cleaning:")
print(df.isnull().sum())

df['Classes'] = df['Classes'].fillna(df['Classes'].mode()[0])


df.to_csv("cleaned_fwi.csv", index=False)

print("Dataset cleaned and saved as cleaned_fwi.csv")
print(df.isnull().sum())

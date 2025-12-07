import pandas as pd

df = pd.read_csv("FWI Dataset.csv")
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.head())
print(df.tail())

print(df[df.isnull().any(axis=1)])
print(df.shape)

df['Region'] = df['Region'].fillna(df['Region'].mode()[0])
df['Classes  '] = df['Classes  '].fillna(df['Classes  '].mode()[0])

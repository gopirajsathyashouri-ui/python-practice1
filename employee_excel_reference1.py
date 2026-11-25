import pandas as pd 

df = pd.read_csv("employee_raw_dataset.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

print(df)
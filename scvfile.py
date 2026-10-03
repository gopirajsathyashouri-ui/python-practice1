import pandas as pd

df = pd.read_csv("new_employee.csv")


df["HighSalary"] = (
    df["Salary"] > 80000
)

df.head()

print(df)
#Employee Records
import pandas as pd
import numpy as np

def fill_missing_age(df):
    return df.fillna(df["Age"].mean())

n = int(input())

data = []

for _ in range(n):
    emp_id, name, age, dept, salary = input().split()

    age = np.nan if age == "NaN" else float(age)

    data.append([
        int(emp_id),
        name,
        age,
        dept,
        float(salary)
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Employee_ID",
        "Name",
        "Age",
        "Department",
        "Salary"
    ]
)

result = fill_missing_age(df)

print(result)

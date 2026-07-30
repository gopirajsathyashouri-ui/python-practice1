# Count Missing Values in Each Column

import pandas as pd
import numpy as np

def count_missing_values(df):
    return df.isnull().sum()

n = int(input())

data = []

for _ in range(n):
    emp_id, name, age, dept, salary = input().split()

    age = np.nan if age == "NaN" else float(age)
    dept = None if dept == "None" else dept
    salary = np.nan if salary == "NaN" else float(salary)

    data.append([emp_id, name, age, dept, salary])

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

print(count_missing_values(df))
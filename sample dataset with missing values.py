import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Ali", "Sara", "Rohan", "Rani", "David"],
    "Age": [25, np.nan, 30, 28, np.nan],
    "Department": ["HR", "IT", None, "Finance", "IT"],
    "Salary": [50000, 60000, np.nan, 55000, 62000]
})

print(employees)
print(employees.isnull())
print(employees.dropna())
print(employees.dropna(axis =1))
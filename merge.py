import pandas as pd 

employees = pd.read_csv("employees.csv")

departments = pd.read_csv("departments.csv")

merged_df = pd.merge(
    employees, 
    departments,
    on = "DepartmentID"
)
print(merged_df)

import pandas as pd

employees = pd.DataFrame({
    "Employee Name": ["Ali", "Sara", "Rohan"],
    "EMPLOYEE_ID": [101, 102, 103],
    "employee-age": [25, 30, 28],
    "Department Name": ["HR", "IT", "Finance"]
})


employees.columns = [
    "employee_name",
    "employee_id",
    "employee_age",
    "department_name"
]
#print(employees)
employees.columns = employees.columns.str.lower()
print(employees)
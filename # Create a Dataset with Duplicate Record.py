# Create a Dataset with Duplicate Records
import pandas as pd 
employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 102, 104, 105, 103],
    "Name": ["Ali", "Sara", "Rohan", "Sara", "Rani", "David", "Rohan"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "IT", "Finance"],
    "Salary": [50000, 60000, 55000, 60000, 55000, 62000, 55000]
})
#print(employees)
#print(employees[employees.duplicated()])
print(employees.drop_duplicates())
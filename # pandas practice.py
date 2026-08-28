# pandas practice 
import pandas as pd 
employee_data = {
    "Name": ["Ali", "Sara", "John", "Priya"],
    "Age": [25, 30, 28, 27],
    "Department": ["IT", "HR", "Finance", "Marketing"],
    "Salary": [50000, 65000, 55000, 60000]
}
df = pd.DataFrame(employee_data)
print(df)
# Export DataFrame to CSV file

import pandas as pd 
data = {
    "EmployeeID": [101, 102, 103],
    "Name": ["Ali", "Sara", "John"],
    "Department": ["IT", "HR", "Finance"],
    "Salary": [50000, 65000, 55000]
}
df = pd.DataFrame(data)
df.to_csv("exported_employee_data.csv", index=False)
new_df = pd.read_csv("exported_employee_data.csv")
print(new_df)
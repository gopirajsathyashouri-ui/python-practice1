import pandas as pd
employee_list = [
    ["Ali", 25, "IT"],
    ["Sara", 30, "HR"],
    ["John", 28, "Finance"],
    ["Priya", 27, "Marketing"]
]

# Convert nested list into DataFrame
df = pd.DataFrame(
    employee_list,
    columns=["Name", "Age", "Department"]
)

# Display DataFrame
print(df)
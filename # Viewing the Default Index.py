# Viewing the Default Index
import pandas as pd
students = {
    "Name": ["Ali", "Sara", "John"],
    "Age": [25, 30, 28]
}
df = pd.DataFrame(students,
                  index=["Student1", "Student2", "Student3"])
print("Students DataFrame:")
print(df)

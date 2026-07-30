# first Pandas program

import pandas as pd

students = {
    "Name": ["Sathya", "Rahul", "Priya"],
    "Age": [23, 22, 24],
    "Marks": [90, 85, 95]
}

df = pd.DataFrame(students)

print(df)
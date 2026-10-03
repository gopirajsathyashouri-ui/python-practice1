import pandas as pd

data = {
    'name': ['Ana', 'Ben', 'Cara', 'Dev', 'Ella'],
    'age': [25, 30, 22, 35, 28],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'salary': [50000, 60000, 45000, 70000, 62000]
}
df = pd.DataFrame(data)
age_sort = df.sort_values('age', ascending = False)
print(age_sort)
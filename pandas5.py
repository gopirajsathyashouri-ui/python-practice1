import pandas as pd

data = {
    'name': ['Ana', 'Ben', 'Cara', 'Dev', 'Ella'],
    'age': [25, 30, 22, 35, 28],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'salary': [50000, 60000, 45000, 70000, 62000]
}
df = pd.DataFrame(data)
df['bonus'] = df['salary'] * 0.1
print(df)
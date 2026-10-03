import pandas as pd

data = {
    'name': ['Ana', 'Ben', 'Cara', 'Dev', 'Ella'],
    'age': [25, 30, 22, 35, 28],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'salary': [50000, 60000, 45000, 70000, 62000]
}
df = pd.DataFrame(data)
print(df.isnull().sum())        # count of NaNs per column
print(df.isnull().values.any()) # single True/False for the whole DataFrame

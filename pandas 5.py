import pandas as pd
df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meera", "Kiran", "Sana", "Dev"],
    "age": [28, 35, 42, 23, 31, 38],
    "city": ["Delhi", "Pune", "Delhi", "Mumbai", "Pune", "Delhi"],
    "salary": [50000, 72000, 95000, 41000, None, 88000]
})
print(df.isna().sum())
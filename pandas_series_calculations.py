import pandas as pd 

temperatures = pd.Series(
    [32, 34, 31, 35, 33],
    index=["Mon", "Tue", "Wed", "Thu", "Fri"]
)


print("Daily Temperatures: ")
print(temperatures)
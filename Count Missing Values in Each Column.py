import pandas as pd 

def count_missing_values(records):
    records_df = pd.DataFrame(records,
                              columns=[
                                  "Employee_id",
                                  "Name",
                                  "Age",
                                  "Department",
                                  "Salary"
                              ])
    records_df = records_df.replace(["NaN", "None"], None)
    missing_counts = records_df.isnull().sum()

    return missing_counts

n = int(input())
records = [input().split() for _ in range(n)]

print(count_missing_values(records))
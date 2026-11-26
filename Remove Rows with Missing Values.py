import pandas as pd 


def remove_missing_rows(records):

    # Step 1: Create DataFrame
    df = pd.DataFrame(
        records,
        columns=[
            "Employee_ID",
            "Name",
            "Age",
            "Department",
            "Salary"
        ]
    )

    # Step 2: Replace missing value indicators
    df = df.replace(["NaN", "None"], None)

    # Step 3: Convert Employee_ID to integers
    df["Employee_ID"] = df["Employee_ID"].astype(int)

    # Step 4: Convert Age and Salary to numeric values
    df["Age"] = pd.to_numeric(df["Age"]).astype(float)
    df["Salary"] = pd.to_numeric(df["Salary"]).astype(float)

    # Step 5: Remove rows with missing values
    cleaned_df = df.dropna()

    # Step 6: Return cleaned DataFrame
    return cleaned_df

n = int(input())
records = [input().split() for _ in range(n)]
print(remove_missing_rows(records))
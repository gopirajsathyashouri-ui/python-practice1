import pandas as pd 

def high_value_customers(df):
    average_spend = df["TotalSpend"].mean()
    total_high_spend = df[df["TotalSpend"] > average_spend]
    return total_high_spend

customers_df= eval(eval(input()))

# Get Result
result_df = high_value_customers(pd.DataFrame(customers_df))
print(result_df.to_string(index=False))


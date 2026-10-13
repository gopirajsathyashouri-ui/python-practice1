import pandas as pd

def calculate_total_quantity_sold(sales_df):
    total_quantity_sold = sales_df.groupby("product_id")["quantity"].sum().reset_index().rename(columns={"quantity":"total_quantity"})
    return total_quantity_sold

sales_df = eval(eval(input()))
# Get Result
result_df = calculate_total_quantity_sold(sales_df)
print(result_df.to_string(index=False))
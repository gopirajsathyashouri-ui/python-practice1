import pandas as pd 

january_sales = pd.read_csv("january_sales.csv")
february_sales = pd.read_csv("february_sales.csv")

sales = pd.concat(
    [january_sales, february_sales],
    axis = 1,
    ignore_index=True
)
print(sales)
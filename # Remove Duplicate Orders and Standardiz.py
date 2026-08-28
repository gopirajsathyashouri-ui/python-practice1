# Remove Duplicate Orders and Standardize Text 
import pandas as pd 
def standardize_orders(order_records):
    columns = [
        "Order_ID",
        "City",
        "Payment_Status"
    ]
    orders_df = pd.DataFrame(order_records, columns=columns)
    orders_df = orders_df.drop_duplicates(subset= "Order_ID", keep= "first")
    orders_df["City"] = orders_df["City"].str.strip().str.title()
    orders_df["Payment_Status"] = orders_df["Payment_Status"].str.strip().str.lower()
    orders_df = orders_df.reset_index(drop=True)
    return orders_df.values.tolist()

def solve():
    n = int(input())

    order_records = []

    for _ in range(n):
        order_id = input()
        city = input()
        payment_status = input()

        order_records.append([
            order_id,
            city,
            payment_status
        ])

    print(standardize_orders(order_records))


solve()
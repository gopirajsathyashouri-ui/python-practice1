import json 
import pandas as pd 

with open("orders_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

items_df = pd.json_normalize(
    data,
    record_path="items",
    meta=[
        "order_id",
        "customer",
        "order_date"
    ]
)

print(items_df)

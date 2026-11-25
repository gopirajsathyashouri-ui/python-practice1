import json
import pandas as pd
# Load JSON data from the file

with open("orders_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

orders_df = pd.json_normalize(data)[
    ["order_id", "customer", "order_date"]
]

print(orders_df)


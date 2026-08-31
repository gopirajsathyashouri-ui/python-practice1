# API Data to DataFrame

import pandas as pd
import requests

url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url, timeout=30)
response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

print(df.head())
print(df.columns)
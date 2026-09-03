import requests

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url, timeout=30)

print("Status code:", response.status_code)
print(response.json()[:2])
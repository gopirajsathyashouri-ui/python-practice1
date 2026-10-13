import requests
BASE_URL = "http://4.186.26.27:8787"
def test_add_employee():
    new_employee = {
        "id": 15,
        "name": "emma",
        "age": 30,
        "gender": "female",
        "department": "sales",
        "salary": 900000
    }
    response = requests.post(f"{BASE_URL}/employees", json=new_employee)
    print("POST /employees:", response.json())

test_add_employee()
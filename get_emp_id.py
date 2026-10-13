import requests
BASE_URL = "http://4.186.26.27:8787"
def test_get_employee_by_id(emp_id):
    response = requests.get(f"{BASE_URL}/employees/{emp_id}")
    print(f"GET /employees/{emp_id}:", response.json())

test_get_employee_by_id(1)
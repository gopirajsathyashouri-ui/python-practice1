import requests
BASE_URL = "http://4.186.26.27:8787"
def test_patch_employee(emp_id):
    updates = {
        "age": 32,
        "salary": 1000000
    }
    response = requests.patch(f"{BASE_URL}/employees/{emp_id}", json=updates)
    print(f"PATCH /employees/{emp_id}:", response.json())

test_patch_employee(10)
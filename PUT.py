import requests
BASE_URL = "http://4.186.26.27:8787"
def test_update_employee(emp_id):
    updated_employee = {
        "id": emp_id,  # ID must match the one being updated
        "name": "emma_updated",
        "age": 31,
        "gender": "female",
        "department": "sales",
        "salary": 950000
    }
    response = requests.put(f"{BASE_URL}/employees/{emp_id}", json=updated_employee)
    print(f"PUT /employees/{emp_id}:", response.json())

test_update_employee(10)
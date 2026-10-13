import requests
BASE_URL = "http://4.186.26.27:8787"
def test_delete_employee(emp_id):
    response = requests.delete(f"{BASE_URL}/employees/{emp_id}")
    print(f"DELETE /employees/{emp_id}:", response.json())
test_delete_employee(10) 
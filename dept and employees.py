departments = {
    "Data Science": ["Aman", "Riya", "Karan"],
    "Marketing": ["Neha", "Rahul"],
    "Finance": ["Simran", "Arjun", "Meera"]
}

for department, employees in departments.items():
    print("Department:", department)

    for employee in employees:
        print("Employee:", employee)
    print()
def get_age(age):
    try:
        converted_age = int(age)
        return converted_age
    except ValueError:
        return "Error: Please enter age as a valid number."
result = get_age("twenty")
print(result)

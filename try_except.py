def get_age(age):
    try:
        age = int(age)
        return age 
    except:
        return "Inavalid input. Please enter a number."

user_age = input("Enter your age: ")
result = get_age(user_age)
print(result)
    
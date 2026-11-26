def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except:
        return "Something went wrong. Please enter valid numbers"

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

result = divide_numbers(num1, num2)
print("Result:", result)
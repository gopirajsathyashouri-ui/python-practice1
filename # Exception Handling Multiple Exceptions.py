# Exception Handling Multiple Exceptions 

try :
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by Zero")
         
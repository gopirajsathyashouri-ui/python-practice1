# Reverse a String 
def reverse_string(string_input): 
     reversed_string = string_input[: : -1]
     return reversed_string
my_string = "Hello, John"
result = reverse_string(my_string)
print(result)

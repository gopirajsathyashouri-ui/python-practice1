input_string = input()
input_char = input()
starts_with = lambda x: True if x.startswith(input_char) else False 
print(starts_with(input_string))
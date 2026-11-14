import numpy as np

def replace_element(arr, to_replace, replacement):
    arr[arr == to_replace] = replacement
    return arr.tolist()

# Reading input dynamically
arr = np.array(eval(input()))
to_replace = int(input())
replacement = int(input())

# Calling the function and displaying the result
print(replace_element(arr, to_replace, replacement))
import numpy as np 

def calculate_std(arr):
    return np.std(arr)

arr = np.array(eval(input()))
print(calculate_std(arr))

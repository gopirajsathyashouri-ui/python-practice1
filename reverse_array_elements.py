import numpy as np 

def reverse_array(arr):
    return arr[: : -1].tolist()

arr = np.array(eval(input()))
print(reverse_array(arr))

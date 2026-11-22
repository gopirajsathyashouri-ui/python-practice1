import numpy as np 

def arrays(arr):
    arr = np.array(arr, dtype=float)
    return arr[: : -1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
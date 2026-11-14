import numpy as np 

def slice_greater_than(arr, threshold):
    return arr[arr > threshold].tolist()

arr = np.array(eval(input()))
threshold = int(input())

print(slice_greater_than(arr, threshold))
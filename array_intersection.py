import numpy as np

def find_intersection(arr1, arr2):
    return np.intersect1d(arr1, arr2).tolist()

arr1 = np.array(eval(input()))
arr2 = np.array(eval(input()))
print(find_intersection(arr1, arr2))

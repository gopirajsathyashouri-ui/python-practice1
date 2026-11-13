import numpy as np 

def element_wise_operations(arr1, arr2):
    addition = arr1 + arr2
    subtraction = arr1 - arr2
    multiplication = arr1 * arr2
    division = arr1 / arr2
    return addition.tolist(), subtraction.tolist(), multiplication.tolist(), division.tolist()

arr1= np.array(eval(input()))
arr2 = np.array(eval(input()))

results = element_wise_operations(arr1, arr2)
for result in results:
    print(result)

    
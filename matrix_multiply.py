import numpy as np

def matrix_multiplication(mat1, mat2):
    return np.dot(mat1, mat2).tolist()

mat1 = eval(input())
mat2 = eval(input())

# Calling the function and displaying the result
result = matrix_multiplication(mat1, mat2)
print(result)
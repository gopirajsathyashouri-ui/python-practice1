import numpy as np

def matrix_multiplication(mat1, mat2):
    mat1_np = np.array(mat1)
    mat2_np = np.array(mat2)
    return np.dot(mat1_np, mat2_np).tolist()

# Reading input dynamically
mat1 = eval(input())
mat2 = eval(input())

# Calling the function and displaying the result
result = matrix_multiplication(mat1, mat2)
print(result)
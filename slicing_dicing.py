import numpy as np 

def extract_submatrix(matrix):
    return matrix[1:4, 1:4].tolist()

matrix = np.array(eval(input()))

# Calling the function and displaying the result
print(extract_submatrix(matrix))

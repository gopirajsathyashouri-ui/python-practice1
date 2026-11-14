import numpy as np

def diagonal_product(matrix):
    return np.prod(np.diag(matrix)).tolist()

matrix = np.array(eval(input()))
print(diagonal_product(matrix))

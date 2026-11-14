import numpy as np

def column_max(matrix):
    return np.max(matrix, axis = 0).tolist()

matrix = np.array(eval(input()))
print(column_max(matrix))
import numpy as np 

def create_diagonal_matrix(values):
    return np.diag(values).tolist()

values = eval(input())
print(create_diagonal_matrix(values))
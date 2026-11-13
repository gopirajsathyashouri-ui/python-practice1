import numpy as np 

def cumulative_sum(arr):
    return np.cumsum(arr).tolist()

arr = np.array(eval(input()))
print(cumulative_sum(arr))

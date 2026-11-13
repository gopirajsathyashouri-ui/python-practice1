import numpy as np

a = [1, 2, 3]
print(a * 2)                    # [1, 2, 3, 1, 2, 3]  (list repeats)

b = np.array([1, 2, 3])
print(b * 2)                    # array([2, 4, 6])    (math on every element)
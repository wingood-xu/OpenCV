import numpy as np

arr1 = np.arange(1, 13).reshape((2, 2, 3))
print(arr1)
print('*' * 50)
arr1[1, 1] = [10, 12, 13]
print(arr1)

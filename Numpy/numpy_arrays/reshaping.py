import numpy as np

array1 = np.array([1, 3, 5, 7, 8, 9, 12, 26, 19, 20])

results = np.reshape(array1, (2, 5))

# print(results)

array2 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
result1 = np.reshape(array2, (4, 2))

print(result1)
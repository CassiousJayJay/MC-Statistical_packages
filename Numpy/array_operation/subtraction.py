import numpy as np

array2 = np.array([1, 2, 3, 4])
array1 = np.array([5, 6, 7, 8])

# using the - operator
result1 = array2 - array1

# using the subtract function
result2 = np.subtract(array2, array1)

print(result1)
print(result2)
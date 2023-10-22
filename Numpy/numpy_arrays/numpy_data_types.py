import numpy as np

array1 = np.array([2, 4, 6, 8, 10])

# print(array1.dtype)

array2 = np.array([1.0, 2.5, 3.7, 4.0])

# print(array2.dtype)

array3 = np.array([2, 4, 6, 8, 10])

float_array = array3.astype("float")

print(float_array, float_array.dtype)
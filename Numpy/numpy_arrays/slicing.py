import numpy as np

# syntax for array numpy array slicing = array[start:stop:step]
# start - index of the first element to be included in the slice
# stop - index of the last element (exclusive)
# step - step size between each element in the slice

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# print(numbers[2:6])

# print(numbers[2:9:2])

# print(numbers[:])

# print(numbers[3:])

# print(numbers[:8])

numbers2 = np.array([2, 4, 6, 8, 10, 12])
# numbers2[1:5:2] = 16

# print(numbers2)

print(numbers2[::-2])



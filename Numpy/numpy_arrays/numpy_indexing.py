import numpy as np

# numbers = np.array([1, 2, 3, 4, 5])

# # numbers[2] = 10
# numbers[-2] = 9

# print(numbers)

results = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])

results[0, 3] = 40

print(results)
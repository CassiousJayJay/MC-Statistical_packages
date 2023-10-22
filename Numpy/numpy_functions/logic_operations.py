import numpy as np

arry1 = np.array([2, 7, 9, 10, 50])
arry2 = np.array([1, 5, 8, 15, 40])

result = np.less(arry1, arry2)
result1 = np.greater(arry1, arry2)
result2 = np.not_equal(arry1, arry2)
result3 = np.greater_equal(arry1, arry2)

# logic operation
x1 = np.array([True, False, True])
x2 = np.array([False, False, True])

# Logical AND
print(np.logical_and(x1, x2))

# Logical OR
print(np.logical_or(x1, x2))

# Logical NOT
print(np.logical_not(x1, x2))



print(result)
print(result1)
print(result2)
print(result3)
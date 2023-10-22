import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])

median = np.median(numbers)

# print(f"The midian is {median}")

array = np.array([[1, 2, 3],
                  [4, 5, 6], 
                  [7, 8, 9]])

result1 = np.median(array, axis=1)
print("The median along the vertical axis is: ", result1)

result2 = np.median(array, axis=0)
print("The median along the horizontal axis is: ", result2)

final_result = np.median(array)
print("The midiam of the entire array is: ", final_result)
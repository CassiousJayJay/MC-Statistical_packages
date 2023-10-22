import numpy as np

array = np.array([[1, 2, 3,], 
                 [4, 5, 6]])

# calculating the mean of the entire array
mean = np.mean(array)

print("The mean for the entire array is: ", mean)

# calculating the mean along the vertical axis

mean_vertical = np.mean(array, axis=0)
print("The mean along the vertical axis is: ", mean_vertical)

# calculating the mean along the horizontal axis

horizontal_mean = np.mean(array, axis=1)
print("The mean along the horizontal axis is: ", horizontal_mean)
import numpy as np

array = np.array([[5, 10, 15, 20],
                  [40, 50, 45, 35]])

final_std = np.std(array)
print("The final std for the entire array is: ", final_std)

# calculating the std along the vertical axis

vertical_std = np.std(array, axis=0)
print("The std along the vertical is: ", vertical_std)

# calculating the std along the horizontal axis
horizontal_std = np.std(array, axis=1)

print("The std along the horizontal is: ", horizontal_std)

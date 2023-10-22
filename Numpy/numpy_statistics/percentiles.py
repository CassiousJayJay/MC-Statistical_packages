import numpy as np

results = np.array([10, 400, 500, 455, 28, 25, 70, 88, 689])

# calculating the 25th percentile
result1 = np.percentile(results, 25)

print("The 25th percentile is: ", result1)

# calculating the 75th percentile
result2 = np.percentile(results, 75)

print("The 75th percentile is: ", result2)
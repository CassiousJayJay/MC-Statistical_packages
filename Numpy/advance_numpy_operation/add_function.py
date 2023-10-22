import numpy as np

array1 = np.array(["Iphone: ", "Price: "])
array2 = np.array(["15", "$15000"])

result = np.char.add(array1, array2)

print(result)
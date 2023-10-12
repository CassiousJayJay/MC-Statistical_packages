import numpy as np
import pandas as pd

arra_1 = np.array([1, 2, 3, 4])
arra_2 = np.array([5, 6, 7, 8])

result_add = arra_1 * arra_2
compare = arra_1 == arra_2

# print(compare)
# print(result_add)

ser = pd.Series([5, 8, 9, 10])
# print(ser)
data = {
    "Name": ["Cassious", "Stephen", "Mark"],
    "Age": [28, 50, 35]
}
df = pd.DataFrame(data)

print(df)
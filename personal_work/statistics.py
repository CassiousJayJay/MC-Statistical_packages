import numpy as np
import pandas as pd
from scipy import stats

data = np.array([10, 200, 30, 10, 400, 10, 50, 60])
data_2 = [10, 200, 30, 10, 400, 10, 50, 60]
# print(np.mean(data))


df = pd.DataFrame(data)
y = df.mean()
# print(y)

result = stats.mode(data)
# print(result)

a = np.ptp(data)
# print(a)
x = np.percentile(data, 25)
y = np.percentile(data, 75)
z = np.mean(data)

# print(x, y, z)

df = pd.DataFrame(data_2)
perc = df.describe(percentiles=[.75, .25])
h = perc.loc["75%"]
i = perc.loc["25%"]
g = perc.loc["50%"]

print(h)
print (i)
print(g)



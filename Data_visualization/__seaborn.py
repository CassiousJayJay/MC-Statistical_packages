import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 30, 40, 50, 60]

df = pd.read_csv("data.csv")

plt.scatter(x, y, color="g", marker="o")
plt.xlabel("Marks")
plt.ylabel("Grades")
plt.title("Results")
# plt.show()

sn.boxplot(x="Ages",y="Names",data=df)

plt.xlabel("Ages")
plt.ylabel("Names")
plt.title("Age Groups")
plt.show()
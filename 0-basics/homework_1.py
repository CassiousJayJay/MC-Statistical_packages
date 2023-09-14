import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as nm


df_csv = pd.read_csv("data.csv")
print(df_csv.head(5))
print(df_csv['Age'].describe())
print(df_csv['Income'].describe())
print(df_csv.isnull())
print(df_csv.value_counts("Category"))
print(df_csv.fillna("Age",))
df_csv["Age"] += 1
print(df_csv)

df = pd.read_csv("data.csv")
sn.boxplot(x="Income", y="Category",data=df)


plt.xlabel("Income")
plt.ylabel("Category")
plt.title("Boxplot")
plt.show()

data = pd.read_csv("data.csv")
plt.hist(data["Age"], bins=10)

plt.xlabel("Value")
plt.ylabel("Age")
plt.title("Histogram")
plt.show()

arr = pd.read_csv("data.csv")
income_values = nm.array(arr["Income"])
final_result = nm.mean(income_values)
print(final_result)





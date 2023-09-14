import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
sn.scatterplot(x="Ages", y="Names",data=df)

plt.xlabel("Ages")
plt.ylabel("Names")
plt.title("Age Groups")
plt.show()
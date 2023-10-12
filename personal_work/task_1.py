import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv("record.csv")
df = df.head(5)
df = df["Name"].describe()
print(df)



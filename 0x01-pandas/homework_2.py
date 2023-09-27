import pandas as pd

df = pd.read_csv("CA-2023-second-term - Sheet1.csv")
# print(df.head(5))
# print(df["task_1"].describe())

filtered_df = df[df('grade') = 'A']

import pandas as pd

df = pd.read_csv("CA-2023-second-term - Sheet1.csv")
df = df.head(5)
df = df["task_1"]
print(df)

# filtered_df = df[df('grade') = 'A']

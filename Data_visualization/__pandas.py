import pandas

lst = pandas.Series([29, 30, 15, 46, 70])

df = pandas.DataFrame({
    "name": ["John", "moses"],
    "ages": [20, 10]
})

df_csv = pandas.read_csv("data.csv")
# print(df)
# df_csv["Ages"] += 1
# df_csv["Gender"] = df_csv["Gender"].map({"Male":"M", "Female":"F"})
print(df_csv.interpolate())
print(df_csv)
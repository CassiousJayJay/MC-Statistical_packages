from scipy.stats import kruskal

data_group1 = [23, 29, 32, 22, 28]
data_group2 = [19, 18, 24, 25, 21]
data_group3 = [16, 15, 14, 17, 20]

stat, p = kruskal(data_group1, data_group2, data_group3)

print(p)
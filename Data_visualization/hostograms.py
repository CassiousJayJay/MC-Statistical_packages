import matplotlib.pyplot as plt


data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
plt.hist(data, bins=5,
         color='purple', edgecolor='black')
plt.xlabel('value')
plt.ylabel('Frequency')
plt.title('Histograms')
plt.show()
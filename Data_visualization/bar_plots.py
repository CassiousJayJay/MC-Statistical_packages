import matplotlib.pyplot as plt

categories = ['category A', 'category B', 'category C']
values = [20, 35, 50]
plt.bar(categories, values, color='g')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar plot')
plt.show()
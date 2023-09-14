import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')
sns.boxplot(x='species', y='sepal_length', data=data)
plt.xlabel('Species')
plt.ylabel('sepal_length')
plt.title('Box Plot of Sepal Length by Species')
plt.show()
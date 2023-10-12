import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

results = np.array([[1, 2, 3, 4, 5], 
                    [5, 6, 7, 8, 9]
                    ])
# results[1][2] = 10
sum_results = np.sum(results)
mean_results = np.mean(results)
results_squared = results ** 2

# print("The sum of all rresults is: ", sum_results)
# print("The mean of the results is: ", mean_results)
print("The result_squared of the results is: ", results_squared)


data = {
    "Name": ["John", "Alice","James", "Chris", "Mark"],
    "Age": [30, 70, 60, 100, 24],
    "Country": ["Zambia", "China", "Congo DR", "America", "England"]
    
}
df = pd.DataFrame(data)
yonug_people = df[df["Age"]> 60] 

average =df["Age"].mean()


print("The average age is: ", average)
print(yonug_people)

#matplotlib

names = ["John", "Mark", "Luke", "James", "Bright"]
grades = [35, 60, 55, 90, 74]

plt.bar(names, grades, color="b")
plt.xlabel("Names")
plt.ylabel("Grades")
plt.title("Results")
plt.show()
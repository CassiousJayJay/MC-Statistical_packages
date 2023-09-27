import matplotlib.pyplot as plt
# import numpy

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales_amount = [15000, 16000, 17000, 20000, 30000, 25000, 32000, 19000, 34000, 28500, 31250, 34000]

plt.bar(months, sales_amount)

plt.xlabel("Months")
plt.ylabel("Sales amount")
plt.title("Sales Data")

plt.show()
plt.savefig("monthly_sales")

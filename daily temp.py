import matplotlib.pyplot as plt 

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temp = [31, 33, 30, 35, 34]

plt.plot(days, temp)
plt.title("Daily Temperature")
plt.xlabel(days)
plt.ylabel(temp)

plt.grid(True)
plt.show()
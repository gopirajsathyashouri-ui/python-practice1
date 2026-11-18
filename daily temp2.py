import matplotlib.pyplot as plt 

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temp = [31, 33, 30, 35, 34]

plt.plot(days, temp, color='r', marker='o', ls="--", label="Temperature")
plt.title("Daily Temperature")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.legend()

plt.grid(True)
plt.show()
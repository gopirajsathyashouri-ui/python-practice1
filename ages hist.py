import matplotlib.pyplot as plt 

ages = [21, 22, 22, 23, 24, 24, 24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 33, 35, 40, 45]

plt.hist(ages, bins=10, edgecolor='black')
plt.title("Ages of people")
plt.show()

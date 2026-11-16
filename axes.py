import matplotlib.pyplot as plt 

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 30, 40])
ax.set_title('My First Chart')
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')

plt.show()
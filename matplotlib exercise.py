import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1, 2)
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 2000, 2500]
profit = [200, 300, 450, 500]

ax[0].plot(months, sales)
ax[0].set_title('Monthly sales')
ax[1].bar(months, profit)
ax[1].set_title("Monthly profit")

plt.show()

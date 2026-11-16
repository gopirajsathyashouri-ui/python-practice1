import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 2000, 2500]

plt.plot(months, sales, color='red', marker='o',
         label='Monthly Sales')

plt.title('Monthly Sales Report')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.legend()
plt.grid()

plt.show()
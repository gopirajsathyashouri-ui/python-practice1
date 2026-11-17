
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 2000, 2500]
profit = [200, 300, 450, 500]
expenses = [800, 900, 1200, 1500]
customers = [100, 150, 180, 250]
orders = [120, 170, 220, 300]
returns = [10, 15, 12, 20]

fig, ax = plt.subplots(2, 3, figsize=(12, 7))

ax[0, 0].plot(months, sales)
ax[0, 0].set_title('Sales')

ax[0, 1].bar(months, profit)
ax[0, 1].set_title('Profit')

ax[0, 2].plot(months, expenses)
ax[0, 2].set_title('Expenses')

ax[1, 0].bar(months, customers)
ax[1, 0].set_title('Customers')

ax[1, 1].plot(months, orders)
ax[1, 1].set_title('Orders')

ax[1, 2].bar(months, returns)
ax[1, 2].set_title('Returns')

fig.suptitle('Company Performance Dashboard')

plt.tight_layout()
plt.show()

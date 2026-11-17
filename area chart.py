import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 2000, 2500]

plt.fill_between(months, sales, alpha=0.5)

plt.plot(months, sales, marker='o')

plt.title('Monthly Sales Area Chart')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()
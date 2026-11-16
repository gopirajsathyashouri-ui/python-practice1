import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [1000, 1500, 2000, 2500]

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    sales,
    color='red',
    linestyle='--',
    linewidth=2,
    marker='o',
    markersize=8,
    markerfacecolor='yellow',
    markeredgecolor='black',
    label='Monthly Sales'
)

plt.title('Monthly Sales Report',
          fontsize=16,
          fontweight='bold')

plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales', fontsize=12)

plt.legend(loc='upper left')
plt.grid(True, linestyle=':', linewidth=0.7)

plt.ylim(0, 3000)

plt.savefig('monthly_sales.png')

plt.show()
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']

sales_2025 = [1000, 1500, 2000, 2500]
sales_2026 = [1200, 1700, 2200, 2800]

plt.plot(months, sales_2025, marker='o', label='2025')
plt.plot(months, sales_2026, marker='s', label='2026')

plt.title('Sales Comparison: 2025 vs 2026')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.legend()
plt.grid()

plt.show()
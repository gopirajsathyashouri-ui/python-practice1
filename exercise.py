import matplotlib.pyplot as plt 

months = ['Jan', 'Feb', 'March', 'Apr']

sales_2024 = [800, 1200, 1600, 2000]
sales_2025 = [1000, 1500, 2000, 2500]
sales_2026 = [1200, 1700, 2200, 2800]

fig, ax = plt.subplots()
ax.plot(months, sales_2024, marker='o', label='2024')
ax.plot(months, sales_2025, marker='s', label='2025')
ax.plot(months, sales_2026, marker='d', label='2026')

ax.set_title('Sales Comparision')
ax.set_xlabel('Months')
ax.set_ylabel('Sales')

ax.legend()
ax.grid()

plt.show()
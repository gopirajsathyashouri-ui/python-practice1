
import matplotlib.pyplot as plt

salaries = [25000, 30000, 35000, 40000, 45000,
            50000, 55000, 60000, 100000]

months = ['Jan', 'Feb', 'Mar', 'Apr']

electronics = [100, 150, 200, 250]
clothing = [80, 100, 120, 150]
food = [50, 70, 90, 100]

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

fig, ax = plt.subplots(2, 3, figsize=(14, 8))

# 1. Box Plot
ax[0, 0].boxplot(salaries)
ax[0, 0].set_title('Salary Box Plot')

# 2. Violin Plot
ax[0, 1].violinplot(salaries)
ax[0, 1].set_title('Salary Violin Plot')

# 3. Heatmap
heatmap = ax[0, 2].imshow(data, cmap='coolwarm')
ax[0, 2].set_title('Heatmap')
fig.colorbar(heatmap, ax=ax[0, 2])

# 4. Area Chart
ax[1, 0].fill_between(months, electronics, alpha=0.5)
ax[1, 0].set_title('Electronics Area Chart')

# 5. Stack Plot
ax[1, 1].stackplot(
    months,
    electronics,
    clothing,
    food,
    labels=['Electronics', 'Clothing', 'Food']
)
ax[1, 1].set_title('Category Sales')
ax[1, 1].legend(fontsize=8)

# 6. Multiple Line Chart
ax[1, 2].plot(months, electronics, marker='o',
              label='Electronics')
ax[1, 2].plot(months, clothing, marker='s',
              label='Clothing')
ax[1, 2].set_title('Sales Comparison')
ax[1, 2].legend()

fig.suptitle('Advanced Data Visualization')
plt.tight_layout()
plt.show()




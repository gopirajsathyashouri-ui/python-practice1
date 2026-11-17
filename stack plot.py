import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr']

electronics = [100, 150, 200, 250]
clothing = [80, 100, 120, 150]
food = [50, 70, 90, 100]

plt.stackplot(
    months,
    electronics,
    clothing,
    food,
    labels=['Electronics', 'Clothing', 'Food']
)

plt.title('Category-wise Sales')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.legend(loc='upper left')

plt.show()

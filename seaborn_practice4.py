import seaborn as sns
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales = [10000, 15000, 12000, 18000, 22000, 25000]

sns.lineplot(x=months, y=sales)

plt.title('Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.show()
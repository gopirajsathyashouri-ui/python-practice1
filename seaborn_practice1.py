import seaborn as sns
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

sales = [1000, 1500, 2000, 1800, 2500]

sns.barplot(x=months, y=sales)

plt.show()
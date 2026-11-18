import seaborn as sns 
import matplotlib.pyplot as plt 

products = ['Mobile', 'Laptop', 'Tablet', 'Watch']

revenue = [50000, 80000, 30000, 20000]

sns.barplot(x=products, y=revenue)
plt.show()
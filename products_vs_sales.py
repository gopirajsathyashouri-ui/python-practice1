import matplotlib.pyplot as plt

products = ['Laptop', 'Mobile', 'Tablet', 'Watch']
sales = [50000, 80000, 30000, 20000]

plt.barh(products, sales)
plt.title('Products vs Sales')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.show()


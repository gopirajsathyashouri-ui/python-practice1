import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales = [12000, 15000, 14000, 18000, 22000, 25000]
profit = [2000, 2500, 2200, 3500, 4500, 5000]

categories = ['Electronics', 'Clothing', 'Furniture', 'Food']
category_sales = [45000, 30000, 25000, 20000]

regions = ['North', 'South', 'East', 'West']
region_profit = [8000, 12000, 7000, 10000]

customer_orders = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40,
                   42, 45, 48, 50, 55, 60, 65, 70, 75, 100]

fig, ax = plt.subplots(2, 3)

ax[0,0].plot(months, sales, marker='o')
ax[0,0].set_title("Monthly sales trend")
ax[0,0].set_xlabel('Months')
ax[0,0].set_ylabel('Sales')

ax[0,0].grid()


ax[0,1].bar(categories, category_sales, color='r')
ax[0,1].set_title("Category-wise Sales")
ax[0,1].set_xlabel('Categories')
ax[0,1].set_ylabel('Sales')

ax[0,2].barh(
    regions, 
    region_profit,
    color=['red', 'blue', 'green', 'orange']
    )
ax[0,2].set_title('Region-wise Profit')
ax[0,2].set_xlabel('Profit')
ax[0,2].set_ylabel('Regions')

ax[1,0].hist(customer_orders, bins=5)
ax[1,0].set_title('Customer Order Distribution')
ax[1,0].set_xlabel('Order Value')
ax[1,0].set_ylabel('Frequency')

ax[1,1].boxplot(customer_orders)

ax[1,1].set_title('Customer Order Outliers')
ax[1,1].set_xlabel('Customer Orders')
ax[1,1].set_ylabel('Order Value')

ax[1,2].plot(months, profit, marker='o')
ax[1,2].set_title('Monthly Profit Trend')
ax[1,2].set_xlabel('Months')
ax[1,2].set_ylabel('Profit')


fig.suptitle('Sales Performance Dashboard', fontsize=16)
plt.tight_layout()
plt.show()
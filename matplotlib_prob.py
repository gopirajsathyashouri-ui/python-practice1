import matplotlib.pyplot as plt 

months = ["Jan", "Feb", "Mar", "Apr", "May"]
product_a = [120, 150, 170, 160, 200]
product_b = [100, 130, 120, 180, 190]

plt.plot(months, product_a, color='blue', marker='o', label='Product A')
plt.plot(months, product_b, color='orange', marker='s', label="Product B")

plt.title("Monthly Sales: Product A vs Product B")
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.legend()
plt.grid(True)

plt.show()
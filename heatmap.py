import matplotlib.pyplot as plt 

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
plt.imshow(data, cmap='coolwarm')

plt.colorbar()
plt.title('Sales Heatmap')

plt.show()
import matplotlib.pyplot as plt 

marks = [45, 50, 55, 60, 60, 65, 70, 75, 80, 90]
plt.violinplot(marks)
plt.title('Student Marks Distribution')
plt.ylabel('Marks')

plt.show()

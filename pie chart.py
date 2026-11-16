import matplotlib.pyplot as plt 

subjects = ['Python', 'SQL', 'Excel', 'Power BI']
hours = [30, 25, 20, 25]

plt.pie(hours, labels=subjects, autopct='%1.1f%%')
plt.show()
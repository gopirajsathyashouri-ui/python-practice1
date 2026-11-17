import matplotlib.pyplot as plt 

salaries = [20000, 25000, 28000, 30000, 32000,
            35000, 38000, 40000, 45000, 100000]
plt.boxplot(salaries)
plt.title('Employee Salary Distribution')
plt.ylabel('Salary')

plt.show()
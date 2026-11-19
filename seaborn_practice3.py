import seaborn as sns
import matplotlib.pyplot as plt

departments = ['HR', 'IT', 'Sales', 'Marketing']

employees = [10, 25, 30, 15]

sns.barplot(
    x=departments,
    y=employees,
    palette='viridis',
    orient='h'
)

plt.title('Department Employees')
plt.xlabel('Department')
plt.ylabel('Employee')
plt.show()
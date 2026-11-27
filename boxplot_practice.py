import seaborn as sns
import matplotlib.pyplot as plt

salaries = [
    20000, 22000, 25000, 28000, 30000,
    32000, 35000, 38000, 40000, 42000,
    45000, 48000, 50000, 55000, 150000
]
sns.boxplot(
    y= salaries,
    color= 'lightgreen'
)
plt.title("Employee Salary Distribution")
plt.ylabel("Salary")
plt.show()
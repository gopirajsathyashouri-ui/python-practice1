import seaborn as sns
import matplotlib.pyplot as plt 

ages = [
    18, 20, 22, 25, 28,
    30, 32, 35, 38, 40,
    22, 25, 28, 30, 35,
    40, 42, 45, 48, 50
]

sns.histplot(
    x= ages,
    bins= 5,
    color= 'orange',
    kde= True,
)
plt.title('Customer Age Distribution')
plt.xlabel('Ages of People')
plt.ylabel('Number of People')
plt.show()
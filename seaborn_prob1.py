import seaborn as sns
import matplotlib.pyplot as plt 

advertising_cost = [1000, 2000, 3000, 4000, 5000, 6000]

sales = [5000, 7000, 9000, 11000, 13000, 16000] 

sns.scatterplot(
    x= advertising_cost,
    y= sales,
    color= 'green',
    s= 100  
)
plt.title('Advertising Cost vs Sales')
plt.xlabel('Cost for Advertising')
plt.ylabel('Sales')
plt.show()
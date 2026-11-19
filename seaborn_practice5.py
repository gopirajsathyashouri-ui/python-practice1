import seaborn as sns
import matplotlib.pyplot as plt 

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

website_visitors = [200, 300, 250, 400, 500, 650]

sns.lineplot(
    x= months,
    y= website_visitors,
    color= 'blue',
    marker= 'o'
)

plt.title('Monthly Website Visitors')
plt.xlabel('Months')
plt.ylabel('No of website visitors')

plt.show()
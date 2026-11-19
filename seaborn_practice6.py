import seaborn as sns 
import matplotlib.pyplot as plt 

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [35, 40, 50, 55, 65, 70, 80, 90]

sns.scatterplot(
    x= study_hours ,
    y=marks
)

plt.title('Study Hours vs Exam Marks')
plt.xlabel('Study Hours')
plt.ylabel('Exam Marks')

plt.show()
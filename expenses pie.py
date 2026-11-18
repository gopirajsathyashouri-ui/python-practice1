import matplotlib.pyplot as plt 

categories = ["Rent", "Food", "Travel", "Savings", "Other"]
amount = [12000, 6000, 3000, 5000, 2000] 

plt.pie(amount, labels = categories, autopct= '%1.1f%%')
plt.title("Expenses on each Category")
plt.show()
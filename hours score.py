import matplotlib.pyplot as plt 

hours = [1, 2, 3, 4, 5, 6, 7, 8]
score = [35, 42, 50, 58, 65, 72, 80, 88] 

plt.scatter(hours, score, alpha=0.5)
plt.xlabel("Hours")
plt.ylabel("Score")
plt.title("Hours Score")
plt.show()
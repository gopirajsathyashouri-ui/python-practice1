import matplotlib.pyplot as plt 

students = ["Asha", "Ravi", "Meena", "Kiran", "Sana"]
marks = [78, 85, 62, 91, 70]

plt.barh(students, marks, color='r')
plt.ylabel("students")
plt.xlabel("marks")
plt.title("Student Marks")
plt.savefig('marks.png', dpi=200)
plt.show()
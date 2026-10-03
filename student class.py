class Student :
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
print("Number of students:", Student.num_students)
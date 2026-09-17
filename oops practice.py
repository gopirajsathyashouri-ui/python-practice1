class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 40:
            return True
        else:
            return False

s1 = Student("Alice", 45)
print(s1.is_pass())
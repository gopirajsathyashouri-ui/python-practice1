class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self,amount):
         self.salary += amount
         print(self.salary)

e1 = Employee("Priya", 50000)
e1.give_raise(5000)  # should print 55000
print(e1)
class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width
    def area(self):
        return self.length * self.width

r1 = Rectangle(4, 2)
r2 = Rectangle(6, 5)

print(r1.area())
print(r2.area())
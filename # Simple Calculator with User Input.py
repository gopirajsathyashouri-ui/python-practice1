# Simple Calculator with User Input

class Calculator:
    def add(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b

a = int(input())
b = int(input())

calc = Calculator()
print(calc.add(a, b))
  

     

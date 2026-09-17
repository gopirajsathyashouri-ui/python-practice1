class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def is_expensive_than(self, other):
        if self.price > other.price:
            return True
        else :
            return False
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)

print(p1.is_expensive_than(p2))  # should print True
print(p2.is_expensive_than(p1))  # should print False
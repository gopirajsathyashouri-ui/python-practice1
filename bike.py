class Bikes:
    def __init__(self, name, model, price):
        self.name = name 
        self.model = model 
        self.price = price 

bike1 = Bikes("Royal Enfiled", 350, 150000)
print("bike name:", bike1.name)
print("model:", bike1.model)
print("price:", bike1.price)


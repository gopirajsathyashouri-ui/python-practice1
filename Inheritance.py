class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(self.brand, "vehicle started")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_details(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Fuel Type:", self.fuel_type)

car1 = Car("Tesla", 120, "Electric")

car1.start()
car1.show_details()
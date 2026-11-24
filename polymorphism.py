class Vehicle:
    def move(self):
        print("Vehicle is moving")
    def fuel_type(self):
        print("Vehicle uses fuel")
class Car(Vehicle):
    def move(self):
        print("Car is moving on road")
    def fuel_type(self):
        print("Car uses petrol or electricity")
class Boat(Vehicle):
    def move(self):
        print("Boat is moving on water")
    def fuel_type(self):
        print("Boat uses diesel")

car = Car()
boat = Boat()

car.move()
car.fuel_type()

print()

boat.move()
boat.fuel_type()
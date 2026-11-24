class Pet:
  def __init__(self, name, age, energy_level):
    self.name = name
    self.age = age
    self.energy_level = energy_level

  def feed(self, a):
    self.energy_level += a

  def play(self, b):
    self.energy_level -= b

  def check_health(self):
    if self.energy_level < 50:
        print("Your pet is not feeling well.")
    else:
        print("Your pet is healthy.")

my_pet = Pet("Buggu", 2, 50)

my_pet.feed(10)
my_pet.play(5)
my_pet.check_health()

print("Health:", my_pet.energy_level)
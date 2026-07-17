#Calculate Dog’s Age in Dog Years

h_age = int(input())
dog_age = 0 
if h_age <= 2 and h_age >= 0:
    dog_age = h_age * 10.5
else :
    dog_age = 21 + (h_age - 2) * 4
print(dog_age)
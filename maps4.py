temps = [0, 20, 37, 100]
def celsius_to_fahrenheit(C):
    F = C * 9/5 + 32
    return F

result = map(celsius_to_fahrenheit, temps)
print(list(result))
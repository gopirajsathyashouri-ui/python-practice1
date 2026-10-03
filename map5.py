a = [1, 2 , 3]
b = [10, 20, 30]
def add(x, y):
    return x + y

result = map(add, a, b)
print(list(result))
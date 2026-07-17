# using map() with a normal function

def square(num):
    return num ** 2
numbers = [1, 2, 3, 4, 5]
result = list(map(square, numbers))
print(result)
  



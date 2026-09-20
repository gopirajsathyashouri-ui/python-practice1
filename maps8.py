pairs = [(1, 2), (3, 4), (5, 6)]
def multiply_pair(pair):
    x, y = pair
    return x * y

print(list(map(multiply_pair, pairs)))
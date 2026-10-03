words = ["hello", "world", "python"]

def to_upper(word):
    return word.upper()

result = map(to_upper, words)
print(list(result))
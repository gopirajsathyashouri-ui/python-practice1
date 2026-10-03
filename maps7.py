s = "hello"

def get_ascii(char):
    return ord(char)

print(list(map(get_ascii, s)))
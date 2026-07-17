# Words with Prime Length

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def find_prime_length_words(text):
    words = text.split()
    result = []

    for word in words:
        if is_prime(len(word)):
            result.append(word)

    return " ".join(result)


# don't touch this
text = input()
result = find_prime_length_words(text)
print(result)
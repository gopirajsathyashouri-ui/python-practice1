def diamond(n):
    # Upper pyramid
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)

    # Inverted pyramid
    for row in range(1, n):
        print(" " * row + "* " * (n - row))


n = 4
diamond(n)
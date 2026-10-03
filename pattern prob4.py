n = 4
for row in range(1, n+1):
    # print leading spaces
    for space in range(n - row):
        print(" ", end="")
    # print stars separated by space
    for column in range(row):
        print("*", end=" ")
    print()
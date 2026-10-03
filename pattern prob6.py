def Hourglass(n):
    for row in range(1, n+1):
        print("* " * n + " " * row)
    for row in range(1, n):
        print("* " * n + " " * row)
    
n = 4
Hourglass(n)
# perfect number

#n = int(input())
def isPerfectNumber(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        return True
    else:
        return False

print(isPerfectNumber(28))
#if total == n:
   # print("Perfect number")
#else:
    #print("Not a perfect number")
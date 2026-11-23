def largest_prime_factor(n):
    largest = None
    f = 2
    while f * f <= n:
        while n % f == 0:   # divide out this factor completely
            largest = f
            n //= f
        f += 1
    if n > 1:               # leftover is a prime
        largest = n
    return largest
n = int(input())
print(largest_prime_factor(n))

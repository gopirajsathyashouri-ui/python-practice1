n = int(input())

step = 1 
while n >= 10:
    total = 0 
    while n > 0:
        total += n % 10 
        n //= 10
    print("Step-" + str(step) + " Sum:", total)
    n = total 
    step += 1 
    
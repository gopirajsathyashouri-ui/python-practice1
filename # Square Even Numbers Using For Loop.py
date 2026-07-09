# Square Even Numbers Using For Loop

numbs = eval(input())
result = []
for num in numbs:
    if num % 2 == 0:
        result.append(num ** 2)
print(result)

lst = eval(input())

result = True
for i in range(len(lst)):
    if i % 2 != lst[i] % 2:
        result = False
        break

print(result)

lst = eval(input())
n = int(input())
result = []
for i in range(len(lst)):
    result.append(lst[i])
    if i < len(lst) - 1:
        result.append(n)
print(result)
items = eval(input())
ch = input()
result = [item for item in items if item.startswith(ch)]
print(result)
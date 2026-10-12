s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        result = [i, i+1]
        break
print(result)
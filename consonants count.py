s = eval(input())
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char not in vowels:
        count += 1
print(count)
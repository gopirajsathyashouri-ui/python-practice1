n = input()
vowels = "aeiouAEIOU"
for i in range(len(n)-2):
    if n[i] not in vowels and n[i+1] in vowels and n[i+2] not in vowels:
        print(n[i : i+3])
        break 
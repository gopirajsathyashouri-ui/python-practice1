s1 = eval(input())
s2 = eval(input())
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
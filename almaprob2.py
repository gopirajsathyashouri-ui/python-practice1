str = input()
def removeDuplicate(str):
    s = ""
    l = str.lower()
    for i in l:
        if i not in s:
            s = s+i
    return s
print(removeDuplicate(str))
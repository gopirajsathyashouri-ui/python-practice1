# Remove duplicates from list of lists
lst = eval(input())
duplicate = []
for lsts in lst:
    if lst.count(lsts) <= 1:
        duplicate.append(lsts)

print(duplicate)
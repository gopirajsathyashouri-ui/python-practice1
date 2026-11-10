list1 = eval(input())
list2 = eval(input())
lst = []
for i in list1 :
    if i not in list2:
        lst.append(i)
for i in list2:
    if i not in list1:
        lst.append(i)
print(lst)
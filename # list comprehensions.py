# list comprehensions

list1 = eval(input())
list2 = eval(input())
 
new_list = [item for item in list1 if item not in list2]
print(new_list)

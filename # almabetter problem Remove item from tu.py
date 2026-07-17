# almabetter problem Remove item from tuple

tup_input = input()
item = input()
tup = tuple(tup_input.split(','))
listx = list(tup)
listx.remove(item)
tup = tuple(listx)
print(tup)


            


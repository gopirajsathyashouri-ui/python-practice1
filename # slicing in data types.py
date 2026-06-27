# slicing in data types

#my_string = "Hello, world!"
#print(my_string[0 : 5])
#print(my_string[7 :])

# my_tuple = (1, 2, 3, 5, 6)
# print(my_tuple[1 : 3])
# print(my_tuple[ : 2])

#my_list = [1, 2, 3, 5, 6]
#print(my_list[2 :])
#print(my_list[ : 3])

my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
subset_dict = dict((key, my_dict[key] ) for key in ['a','c'])
print(subset_dict)



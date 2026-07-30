#Remove duplicate elements

num_element = int(input())
array = []
for i in range(num_element):
    num = int(input(f"Enter the element between 0 to {num_element - 1}:"))
    array.append(num)

new_array = []
for i in array:
    if i not in new_array:
        new_array.append(i)

print("Array elements after removing duplicates")

for i in new_array:
    print(i)




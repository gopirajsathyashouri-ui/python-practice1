#pythonarraymethods.py"

arr = [10, 20, 30]
print("Original array:", arr)

arr.append(40)
print("Array after append:", arr)

arr.insert(1, 15)
print("Array after insert:", arr)

arr.extend([50, 60])
print("Array after extend:", arr)

arr.remove(15)
print("Array after remove:", arr)

arr.pop()
print("Array after pop:", arr)

print("Index of 30:", arr.index(30))
print("Count of 20:", arr.count(20))

arr.sort()
print("Array after sort:", arr)

arr.sort(reverse=True)
print("Descending sort:", arr)

arr.reverse()
print("Reversed list:", arr)
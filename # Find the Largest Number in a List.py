# Find the Largest Number in a List
numbers = [15, 42, 8, 96, 31]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest Number:", largest)
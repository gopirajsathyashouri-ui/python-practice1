#nestedforlopps.py

numbers = [
    [2, 5, 11, 20, 8],
    [9, 4, 15, 28, 17],
    [1, 6, 21, 18, 3],
    [10, 13, 25, 33, 30],
    [14, 7, 16, 19, 22]
]
even_count = 0
odd_count = 0
for sublist in numbers:
    for num in sublist:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
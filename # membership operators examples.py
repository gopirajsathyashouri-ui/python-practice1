# membership operators examples

print("\n--- List Examples ---")
subjects = ["Math", "Science", "English"]
print("Math" in subjects)
print("Science" in subjects)
print("English" not in subjects)
print("Physics" not in subjects)
print("\n---Tuple examples---")
colors = ("Green", "Red", "White")
print("Green" in colors)
print("Red" not in colors)
print("White" in colors)
print("\n---set examples---")
numbers = {10, 20, 30, 40}
print(20 in numbers)
print(55 in numbers)
print(45 not in numbers)
print("\n--- Dictionary Examples (checking keys) ---")
student = {"name" : "Alice", "age" : "24", "course" : "Python"}
print("Alice" in student.values())
print("name" not in student)
print("age" in student) 
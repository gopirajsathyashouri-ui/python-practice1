# Nested Loop with List of Lists

marks = [
    [80, 85, 89],
    [70, 75, 78],
    [88, 92, 95]
]

for student_marks in marks:
    for mark in student_marks :        
        print(mark)
def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    return marks 

try:
    student_marks = validate_marks(90)
    print("Marks:", student_marks)
except ValueError as error:
    print("Error:", error)
    
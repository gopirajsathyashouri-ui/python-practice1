# panda series from marks
import pandas as pd

def create_marks_series(marks):
    student_marks = pd.Series(marks)
    return student_marks
n = int(input())
marks = list(map(int, input().split()))
result = create_marks_series(marks)
print(result)





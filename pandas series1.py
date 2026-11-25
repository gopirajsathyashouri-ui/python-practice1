import pandas as pd 

def create_student_series(names, marks):
    student_series = pd.Series(names, marks)
    return student_series

n = int(input())
names = input().split()
marks = list(map(int, input().split()))
result = create_student_series(names, marks)
print(result)
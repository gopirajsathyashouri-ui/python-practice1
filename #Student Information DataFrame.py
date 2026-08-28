#Student Information DataFrame 
import pandas as pd 
student_data = {
    "Name": ["Ali", "Sara", "John", "Priya"],
    "Age": [20, 21, 19, 22],
    "Course": ["Python", "Web Development", "SQL", "Machine Learning"]
}
print("Student Data:")
student_df = pd.DataFrame(student_data)
print(student_df)
# Understanding Index Alignment
import pandas as pd 
marks = pd.Series([89, 92, 95], index = ['Math', 'Science', 'English'])
bonus = pd.Series([5, 5, 5], index = ['Math', 'Science', 'English'])
total = marks + bonus
print(total)
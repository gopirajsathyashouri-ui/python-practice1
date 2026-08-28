# Creating and Analyzing Exam Results

import pandas as pd
results = {
    "Student": ["Ali", "Sara", "John", "Priya"],
    "Math": [85, 92, 78, 88],
    "Science": [90, 87, 82, 95]
}
results_df = pd.DataFrame(results)
print("Exam Results:")
print(results_df)
print()
print("Average marks:")
print(results_df["Math"].mean())
print(results_df["Science"].mean())
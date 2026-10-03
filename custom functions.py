import pandas as pd

df = pd.read_csv("new_employee.csv")
def experience_level(exp):

    if exp < 3:
        return "Junior"

    elif exp < 7:
        return "Mid-Level"

    else:
        return "Senior"


df["ExperienceLevel"] = df["Experience"].apply(
    experience_level
)

df.head()
print(experience_level(5))
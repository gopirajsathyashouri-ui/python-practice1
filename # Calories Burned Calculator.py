# Calories Burned Calculator

def calculate_calories_burned(duration_mins, activity):
    calories_burned = 0
    while duration_mins > 0:
        if activity == "running" :
            calories_burned += 10
        elif activity == "swimming":
            calories_burned += 8
        elif activity == "cycling":
            calories_burned += 6
        else :
            return "Invalid activity type."
        duration_mins -= 1
    return f"You burned {calories_burned} calories during the {activity} workout."


result = calculate_calories_burned(duration_mins=20, activity="running")
print(result)             


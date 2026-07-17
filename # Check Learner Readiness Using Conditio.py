# Check Learner Readiness Using Conditions

is_active_learner = input() 
completed_activities_raw = input()
quiz_score_raw = input()
attendance_percentage = float(input())

completed_activities = int(completed_activities_raw)
quiz_score = float(quiz_score_raw)

print("Active Check:", is_active_learner)
print("Activity Check:", completed_activities >= 6)
print("Score Check:", quiz_score >= 70)
print("Attendance Check:", attendance_percentage >= 80)

if is_active_learner == "True" and completed_activities >= 6 and quiz_score >= 70 and attendance_percentage >= 80:
    print("Readiness Status: Ready for the next control flow practice.")
else :
    print("Readiness Status: Needs more practice before continuing.")
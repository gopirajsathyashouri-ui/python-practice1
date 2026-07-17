#Check Learner Readiness

is_active_learner = True
lessons_completed = 3
quiz_score = 70
active_check = is_active_learner
lessons_check = lessons_completed >= 3
score_check = quiz_score >= 70
ready = active_check and lessons_check and score_check
print(f"Active check: {active_check}")
print(f"Lessons check: {lessons_check}")
print(f"Score check: {score_check}")
print(f"Ready for next chapter: {ready}")
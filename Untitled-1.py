# almabetter Validate Topics and Weekly Tasks

learning_topics = ["Prompt Engineering", "Python Programming", "Machine Learning"]
weekly_tasks = ["Attempt Quiz", "Read Machine Learning paper", "Projects"]
prompt_available = "Prompt Engineering" in learning_topics
loops_available = "Loops" in learning_topics
attempt_quiz = "Attempt Quiz" in weekly_tasks
submit_project = "Submit Project" not in weekly_tasks
print(f"Prompt Engineering Available: {prompt_available}")
print(f"Loops Available: {loops_available}")
print(f"Attempt Quiz Available: {attempt_quiz}")
print(f"Submit Project Available: {submit_project}")
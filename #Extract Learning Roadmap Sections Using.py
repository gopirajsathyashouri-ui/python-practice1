#Extract Learning Roadmap Sections Using Slicing
lessons = [ "Decoding an AI-Powered MultiPDF RAG Agentic Architecture", "Getting Started with Python & Prompt Engineering", "Data Types & Operators in Python", "Indexing & Slicing" ] 
learning_topics = [ "Python", "Variables", "Data Types", "Operators", "Indexing", "Slicing", "Prompt Engineering" ] 
chapter_name = "Python Fundamentals" 
student_city = "Bengaluru" 
print(f"First Two Lessons: {lessons[0 :2]}")
print(f"Last Two Lessons: {lessons[-2 :]}")
print(f"Lessons Except First: {lessons[1 : ]}")
print(f"Alternate Topics: {learning_topics[0 : : 2]}")
print(f"Reversed Topics: {learning_topics[ : : -1]}")
print(f"First 10 Characters of Chapter Name: {chapter_name[0 : 10]}")
print(f"Last 12 Characters of Chapter Name: {chapter_name[-12 : ]}")
print(f"Reversed City: {student_city[ : : -1]}")

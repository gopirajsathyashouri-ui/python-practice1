questions = [
    {
        "question": "Who scored first double hundred in ODIs ?",
        "options": ["A. Sachin", "B. Dhoni", "C. Kohli", "D. Dravid"],
        "answer": "A"
    },
    {
        "question": "Who has the highest score in ODIs ?",
        "options": ["A. Sachin", "B. Sehwag", "C. Rohit", "D. Guptill"],
        "answer": "C"
    },
    {
        "question": "Who has the highest wickets in Test ?",
        "options": ["A. Warne", "B. Muralitharan", "C. Kumble", "D. Ashwin"],
        "answer": "B"
    },
    {
        "question": "Which team won first ODI World Cup ?",
        "options": ["A. India", "B. Australia", "C. West Indies", "D. England"],
        "answer": "C"
    }
]
score = 0
for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    player = input("Your answer (A/B/C/D): ").upper()

    if player == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", q["answer"])
print("\nQuiz finished!")
print("Your score:", score, "/", len(questions))

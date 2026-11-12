import random 

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
print("Computer's pick: ", computer)
player = input("Enter Rock, Paper, Scissors: ")
if player == computer:
    print("It's a tie!")
elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
    print("You win!")
else:
    print("Computer wins!")

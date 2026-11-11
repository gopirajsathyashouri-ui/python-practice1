import random 
num = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess the number:"))
    attempts += 1
    if guess == num:
        print("Correct! you guessed right")
        break
    elif num-5 < guess < num or num + 5 > guess > num:
        print("Too close! Try again")
    elif guess < num-5:
        print("Too low! Try again")
    else :
        print("Too high! Try again")

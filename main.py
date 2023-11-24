import random

options = ["rock", "paper", "scissors"]

def play():
    user_input = input("Rock, Paper or Scissors?: ").lower()
    if user_input in options:
        computer = random.choice(options)
        if user_input == computer:
            print("Your opponent played: " + computer)
            print("It's a tie.")
        elif user_input == "rock" and computer == "paper":
            print("Your opponent played: " + computer)
            print("Better luck next time.")
        elif user_input == "paper" and computer == "scissors":
            print("Your opponent played: " + computer)
            print("Better luck next time.")
        else:
            print("Your opponent played: " + computer)
            print("Yey! You win.")
            x = False
    else:
        print("Incorrect input. Try again.")

while True:
    play()
import random

def rps():
    choices = ["rock", "paper", "scissors"]

    print("=== Rock – Paper – Scissors ===")
    print("Type rock, paper, or scissors. Type quit to stop.")

    while True:
        user = input("\nYour choice: ").lower()

        if user == "quit":
            print("Goodbye!")
            break

        if user not in choices:
            print("Invalid choice! Choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print("Computer chose:", computer)

        # Determine winner
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You WIN!")
        else:
            print("You LOSE!")

# Run the game
rps()
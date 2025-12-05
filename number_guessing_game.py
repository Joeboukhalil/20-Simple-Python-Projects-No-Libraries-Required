#!/usr/bin/env python3
"""
Number Guessing Game
- Computer picks a number
- User tries to guess it
- Hints provided: Too high / Too low
"""

import random

def main():
    print("=== Number Guessing Game ===")
    while True:
        try:
            lower = int(input("Enter the lower bound: "))
            upper = int(input("Enter the upper bound: "))
            if lower >= upper:
                print("Lower bound must be less than upper bound.")
                continue
            break
        except ValueError:
            print("Enter valid integers.")

    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"\nI have picked a number between {lower} and {upper}. Try to guess it!")

    while True:
        guess = input("Your guess (or 'quit' to exit): ").strip()
        if guess.lower() == "quit":
            print(f"The number was {secret_number}. Goodbye!")
            break
        try:
            guess = int(guess)
            attempts += 1
            if guess < secret_number:
                print("Too low! 🔽")
            elif guess > secret_number:
                print("Too high! 🔼")
            else:
                print(f"Correct! 🎉 You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Enter a valid integer.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Flashcards Memory Trainer (Pure Python)
- Create flashcards
- Test yourself
- Track correct answers
- Save and load flashcards in a text file
"""

import os
import random

FLASH_FILE = "flashcards.txt"

def load_flashcards():
    flashcards = []
    if os.path.exists(FLASH_FILE):
        with open(FLASH_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if "||" in line:
                    question, answer = line.split("||", 1)
                    flashcards.append({"q": question, "a": answer})
    return flashcards

def save_flashcards(flashcards):
    with open(FLASH_FILE, "w") as f:
        for card in flashcards:
            f.write(f"{card['q']}||{card['a']}\n")

def add_flashcard(flashcards):
    question = input("Enter the question: ").strip()
    answer = input("Enter the answer: ").strip()
    if question and answer:
        flashcards.append({"q": question, "a": answer})
        save_flashcards(flashcards)
        print("Flashcard added.")

def test_flashcards(flashcards):
    if not flashcards:
        print("No flashcards available. Add some first.")
        return
    flashcards_copy = flashcards[:]
    random.shuffle(flashcards_copy)
    correct = 0

    for idx, card in enumerate(flashcards_copy, 1):
        print(f"\nFlashcard {idx}: {card['q']}")
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == card['a'].lower():
            print("Correct! ✅")
            correct += 1
        else:
            print(f"Wrong! ❌ Correct answer: {card['a']}")

    print("\n=== Test Completed ===")
    print(f"Score: {correct} / {len(flashcards_copy)}")
    if correct == len(flashcards_copy):
        print("Perfect! 🌟")
    elif correct >= len(flashcards_copy)//2:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")

def show_flashcards(flashcards):
    if not flashcards:
        print("No flashcards available.")
        return
    print("\nCurrent flashcards:")
    for idx, card in enumerate(flashcards, 1):
        print(f"{idx}. Q: {card['q']} | A: {card['a']}")

def delete_flashcard(flashcards):
    show_flashcards(flashcards)
    if not flashcards:
        return
    try:
        num = int(input("Enter flashcard number to delete: "))
        if 1 <= num <= len(flashcards):
            card = flashcards.pop(num-1)
            save_flashcards(flashcards)
            print(f"Deleted flashcard: {card['q']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    flashcards = load_flashcards()
    print("=== Flashcards Memory Trainer ===")

    while True:
        print("\nMenu:")
        print("1. Add flashcard")
        print("2. Test yourself")
        print("3. Show all flashcards")
        print("4. Delete a flashcard")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_flashcard(flashcards)
        elif choice == "2":
            test_flashcards(flashcards)
        elif choice == "3":
            show_flashcards(flashcards)
        elif choice == "4":
            delete_flashcard(flashcards)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()
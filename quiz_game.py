#!/usr/bin/env python3
"""
Simple Quiz Game (Pure Python)
- Multiple-choice questions
- Score tracking
- End-of-quiz results
"""

def main():
    print("=== Welcome to the Quiz Game ===\n")
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "B"
        },
        {
            "question": "Which programming language is this game written in?",
            "options": ["A) Java", "B) C++", "C) Python", "D) JavaScript"],
            "answer": "C"
        },
        {
            "question": "What is 7 + 8?",
            "options": ["A) 14", "B) 15", "C) 16", "D) 17"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "answer": "B"
        }
    ]

    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Please choose A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer is {q['answer']}.")

    print("\n=== Quiz Finished ===")
    print(f"Your score: {score} out of {len(questions)}")

    if score == len(questions):
        print("Perfect score! 🎉")
    elif score >= len(questions)//2:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")

if __name__ == "__main__":
    main()
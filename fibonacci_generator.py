#!/usr/bin/env python3
"""
Fibonacci Generator
- Print Fibonacci sequence up to N terms
"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("=== Fibonacci Generator ===")
    while True:
        inp = input("Enter number of terms (or 'quit' to exit): ").strip()
        if inp.lower() == "quit":
            print("Goodbye!")
            break
        try:
            n = int(inp)
            if n <= 0:
                print("Enter a positive integer.")
                continue
            seq = fibonacci(n)
            print(f"First {n} Fibonacci numbers:")
            print(seq)
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
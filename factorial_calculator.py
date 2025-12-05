#!/usr/bin/env python3
"""
Factorial Calculator
- Recursive and iterative versions
"""

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    print("=== Factorial Calculator ===")
    while True:
        inp = input("Enter a non-negative integer (or 'quit' to exit): ").strip()
        if inp.lower() == "quit":
            print("Goodbye!")
            break
        try:
            n = int(inp)
            if n < 0:
                print("Enter a non-negative integer.")
                continue

            print(f"\nFactorial of {n}:")
            print(f"Iterative: {factorial_iterative(n)}")
            print(f"Recursive: {factorial_recursive(n)}")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
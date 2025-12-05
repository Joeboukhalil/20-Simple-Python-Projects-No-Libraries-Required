#!/usr/bin/env python3
"""
Prime Number Checker
- Detects if a number is prime
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    print("=== Prime Number Checker ===")
    while True:
        inp = input("Enter a number (or 'quit' to exit): ").strip()
        if inp.lower() == "quit":
            print("Goodbye!")
            break
        try:
            num = int(inp)
            if is_prime(num):
                print(f"{num} is a PRIME number ✅")
            else:
                print(f"{num} is NOT a prime number ❌")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
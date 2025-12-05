#!/usr/bin/env python3
"""
Prime Number Generator
- Generate all primes up to a limit
- Generate first N primes
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

def primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    print("=== Prime Number Generator ===")
    while True:
        print("\nOptions:")
        print("1. Generate all primes up to a number")
        print("2. Generate first N primes")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            try:
                limit = int(input("Enter the upper limit: "))
                primes = primes_up_to(limit)
                print(f"Primes up to {limit}:")
                print(primes)
            except ValueError:
                print("Enter a valid integer.")
        elif choice == "2":
            try:
                n = int(input("Enter how many primes to generate: "))
                primes = first_n_primes(n)
                print(f"First {n} primes:")
                print(primes)
            except ValueError:
                print("Enter a valid integer.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-3.")

if __name__ == "__main__":
    main()
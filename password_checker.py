#!/usr/bin/env python3
"""
Password Strength Checker (Pure Python)
Checks passwords for:
- Length
- Use of lowercase, uppercase, digits, symbols
- Weak password patterns
"""

import string

# Optional: common weak passwords (add more if you like)
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "letmein", "monkey", "dragon", "111111", "iloveyou"
]

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>/?"

def check_strength(password):
    strength = 0
    notes = []

    length = len(password)

    # Length
    if length >= 12:
        strength += 2
    elif length >= 8:
        strength += 1
    else:
        notes.append("Password is too short (less than 8 characters).")

    # Character variety
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    count_types = sum([has_lower, has_upper, has_digit, has_symbol])
    if count_types == 4:
        strength += 2
    elif count_types == 3:
        strength += 1
    else:
        notes.append("Use a mix of uppercase, lowercase, digits, and symbols.")

    # Common passwords
    if password.lower() in COMMON_PASSWORDS:
        notes.append("This is a very common password. Avoid it!")
        strength = 0

    # Simple patterns (like all digits, or same letter repeated)
    if password.isdigit():
        notes.append("All digits - easy to guess!")
        strength = min(strength, 1)
    if len(set(password)) <= 2:
        notes.append("Too few unique characters - easy to guess!")
        strength = min(strength, 1)

    # Determine final strength
    if strength >= 4:
        rating = "Very Strong"
    elif strength == 3:
        rating = "Strong"
    elif strength == 2:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, notes

def main():
    print("=== Password Strength Checker ===")
    print("Enter 'quit' to exit.\n")
    while True:
        pwd = input("Enter password to check: ").strip()
        if pwd.lower() == "quit":
            print("Goodbye!")
            break
        rating, notes = check_strength(pwd)
        print(f"\nPassword strength: {rating}")
        if notes:
            print("Notes:")
            for n in notes:
                print(" -", n)
        print("\n" + "-"*40)

if __name__ == "__main__":
    main()
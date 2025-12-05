#!/usr/bin/env python3
"""
Password Generator (pure Python, built-in modules only)

Features:
- Choose length
- Toggle inclusion: lowercase, uppercase, digits, symbols
- Option to exclude ambiguous characters (like i, l, 1, O, 0)
- Generate multiple passwords at once
- Shows estimated entropy (bits) for each password
"""

import secrets
import string
import math

AMBIGUOUS = "Il1O0"

def build_charset(use_lower, use_upper, use_digits, use_symbols, exclude_ambiguous):
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        # a conservative set of symbols useful in passwords
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"
    if exclude_ambiguous:
        charset = "".join(ch for ch in charset if ch not in AMBIGUOUS)
    return charset

def estimate_entropy(charset_len, length):
    # entropy in bits = length * log2(charset_size)
    if charset_len <= 1:
        return 0.0
    return length * math.log2(charset_len)

def generate_password(charset, length):
    return "".join(secrets.choice(charset) for _ in range(length))

def yes_no_prompt(prompt, default=True):
    if default:
        choices = "Y/n"
    else:
        choices = "y/N"
    while True:
        ans = input(f"{prompt} ({choices}): ").strip().lower()
        if ans == "" and default is not None:
            return default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer yes or no (y/n).")

def int_prompt(prompt, default, min_val=1, max_val=1024):
    while True:
        val = input(f"{prompt} (default {default}): ").strip()
        if val == "":
            return default
        try:
            n = int(val)
            if n < min_val or n > max_val:
                print(f"Enter a number between {min_val} and {max_val}.")
                continue
            return n
        except ValueError:
            print("Enter a valid integer.")

def main():
    print("=== Password Generator ===\n")

    length = int_prompt("Password length", 16, 4, 256)
    count = int_prompt("How many passwords to generate", 5, 1, 50)

    use_lower = yes_no_prompt("Include lowercase letters?", True)
    use_upper = yes_no_prompt("Include uppercase letters?", True)
    use_digits = yes_no_prompt("Include digits?", True)
    use_symbols = yes_no_prompt("Include symbols (e.g. !@#$)?", False)
    exclude_amb = yes_no_prompt("Exclude ambiguous characters (Il1O0)?", True)

    charset = build_charset(use_lower, use_upper, use_digits, use_symbols, exclude_amb)
    if not charset:
        print("Error: character set is empty. Enable at least one category.")
        return

    entropy = estimate_entropy(len(charset), length)
    print(f"\nCharset size: {len(charset)} characters")
    print(f"Estimated entropy per password: {entropy:.1f} bits\n")

    print("Generated passwords:")
    for i in range(count):
        pwd = generate_password(charset, length)
        print(f"{i+1:2d}. {pwd}  (entropy: {estimate_entropy(len(charset), len(pwd)):.1f} bits)")

    # Option to save to file
    save = yes_no_prompt("\nSave these passwords to a file?", False)
    if save:
        filename = input("Filename (default passwords.txt): ").strip() or "passwords.txt"
        try:
            with open(filename, "w") as f:
                f.write(f"# Generated {count} passwords (length {length})\n")
                f.write(f"# Charset size: {len(charset)}  Estimated entropy: {entropy:.1f} bits\n\n")
                for i in range(count):
                    f.write(generate_password(charset, length) + "\n")
            print(f"Passwords saved to {filename}")
        except Exception as e:
            print("Failed to save file:", e)

    print("\nDone. Keep your passwords secure!")

if __name__ == "__main__":
    main()
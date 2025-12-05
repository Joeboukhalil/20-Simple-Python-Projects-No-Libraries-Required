#!/usr/bin/env python3
"""
String Tools
- Reverse a sentence
- Check if a string is a palindrome
"""

def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

def is_palindrome(s):
    s_clean = "".join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]

def main():
    print("=== String Tools ===")
    while True:
        print("\nOptions:")
        print("1. Reverse a sentence")
        print("2. Check if a string is a palindrome")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            sentence = input("Enter a sentence to reverse: ")
            reversed_sentence = reverse_sentence(sentence)
            print(f"Reversed sentence: {reversed_sentence}")
        elif choice == "2":
            string_input = input("Enter a string to check palindrome: ")
            if is_palindrome(string_input):
                print("✅ It is a palindrome!")
            else:
                print("❌ It is NOT a palindrome.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-3.")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Caesar Cipher Encryption / Decryption
- Shift letters by a key
- Only shifts alphabet letters, keeps other characters unchanged
"""

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

def main():
    print("=== Caesar Cipher ===")
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter text to encrypt: ")
            try:
                key = int(input("Enter shift key (integer): "))
                encrypted = encrypt(text, key)
                print(f"Encrypted text: {encrypted}")
            except ValueError:
                print("Enter a valid integer key.")
        elif choice == "2":
            text = input("Enter text to decrypt: ")
            try:
                key = int(input("Enter shift key (integer): "))
                decrypted = decrypt(text, key)
                print(f"Decrypted text: {decrypted}")
            except ValueError:
                print("Enter a valid integer key.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-3.")

if __name__ == "__main__":
    main()
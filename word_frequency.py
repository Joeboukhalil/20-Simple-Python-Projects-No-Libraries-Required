#!/usr/bin/env python3
"""
Word Frequency Counter
- Counts occurrences of each word in a text
"""

def count_words(text):
    text = text.lower()
    # Remove punctuation
    for ch in ",.!?;:\"()[]{}":
        text = text.replace(ch, " ")
    words = text.split()
    
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def main():
    print("=== Word Frequency Counter ===")
    while True:
        print("\nOptions:")
        print("1. Enter text manually")
        print("2. Read text from file")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter your text:\n")
        elif choice == "2":
            filename = input("Enter file name: ").strip()
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
            except FileNotFoundError:
                print("File not found!")
                continue
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-3.")
            continue

        freq = count_words(text)
        print("\nWord Frequencies:")
        for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
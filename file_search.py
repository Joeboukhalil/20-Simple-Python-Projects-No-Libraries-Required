#!/usr/bin/env python3
"""
File Search Tool
- Search for a word or phrase inside files
- Shows matching lines with line numbers
"""

import os

def search_in_file(filename, search_term):
    matches = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                if search_term.lower() in line.lower():
                    matches.append((i, line.strip()))
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    return matches

def main():
    print("=== File Search Tool ===")
    while True:
        search_term = input("\nEnter word or phrase to search (or 'quit' to exit): ").strip()
        if search_term.lower() == "quit":
            print("Goodbye!")
            break

        files = input("Enter file names (comma-separated): ").strip().split(",")
        files = [f.strip() for f in files]

        for filename in files:
            print(f"\nSearching in '{filename}':")
            matches = search_in_file(filename, search_term)
            if matches:
                for lineno, line in matches:
                    print(f"Line {lineno}: {line}")
                print(f"Total matches: {len(matches)}")
            else:
                print("No matches found.")

if __name__ == "__main__":
    main()
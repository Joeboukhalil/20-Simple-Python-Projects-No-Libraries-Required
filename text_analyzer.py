#!/usr/bin/env python3
"""
Text Analyzer
- Counts characters, words, sentences, and paragraphs in a file
"""

def analyze_text(text):
    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    paragraphs = [p for p in text.split('\n') if p.strip() != '']
    num_paragraphs = len(paragraphs)
    return num_chars, num_words, num_sentences, num_paragraphs

def main():
    print("=== Text Analyzer ===")
    while True:
        filename = input("\nEnter filename to analyze (or 'quit' to exit): ").strip()
        if filename.lower() == "quit":
            print("Goodbye!")
            break
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print("File not found! Try again.")
            continue

        chars, words, sentences, paragraphs = analyze_text(text)
        print(f"\nAnalysis of '{filename}':")
        print(f"Characters: {chars}")
        print(f"Words: {words}")
        print(f"Sentences: {sentences}")
        print(f"Paragraphs: {paragraphs}")

if __name__ == "__main__":
    main()
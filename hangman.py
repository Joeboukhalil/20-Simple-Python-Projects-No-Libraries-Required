import random

def choose_word():
    words = [
        "python", "adventure", "hangman", "challenge", "terminal",
        "wizard", "forest", "castle", "android", "puzzle",
        "magic", "dragon", "science", "robot", "galaxy"
    ]
    return random.choice(words)

def display_word(word, guessed):
    result = ""
    for letter in word:
        if letter in guessed:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()

def hangman():
    print("=== Hangman Game ===")
    word = choose_word()
    guessed_letters = []
    attempts = 6  # number of wrong guesses allowed

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed:", " ".join(guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter ONE letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong!")
            attempts -= 1

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\nYou WIN! The word was:", word)
            return

    print("\nYou lost! The word was:", word)

# Run the game
hangman()
import random

# Load the list of possible words from an external file.
with open("C:/Users/thoma/Projects/word-guessing-game/data/words.txt") as textFile:
    words = textFile.readlines()

# Randomly select one word and strip whitespace/newlines.
random_word = random.choice(words).strip()

name = input("What is your name? ")
print(f"Good luck! {name}")

print("A 5 letter word has been chosen. Use Capitals in order to guess.")
print("Guess the characters: ")

# Store all letters the user has guessed so far.
guesses = ''

# Number of attempts allowed before the player loses.
turns = 12

# Main game loop.
while turns > 0:
    failed = 0  

    # Letters that have been guessed are shown, others are hidden as underscores.
    for char in random_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1  

    # If no letters are hidden, the player has guessed the full word.
    if failed == 0:
        print(f"Congratulations {name}. You win!")
        print(f"The word was {random_word}.")
        break

    print()
    guess = input("Guess a character: ")

    # Input validation section.
    if not guess.isalpha():
        # Ensures only letters are accepted.
        print('Enter only a LETTER')
        continue
    elif len(guess) > 6:
        # Prevents guessing long strings.
        print('Enter only a FIVE letter word')
        continue
    elif guess in guesses:
        # Avoids penalizing the player for repeated guesses.
        print('You have already guessed that letter')
        continue
    elif guess not in random_word:
        # Incorrect guess: reduce remaining turns and give feedback.
        turns -= 1
        print("Wrong!")
        print(f"You have {turns} more guesses.")

        # Check if the player has run out of turns.
        if turns == 0:
            print("Oh no! You lost!")
            print(f"The word was {random_word}")
        continue

    # If the guess is valid and correct, add it to the guessed letters.
    guesses += guess

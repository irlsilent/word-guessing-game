import random

with open("C:/Users/thoma/Projects/word-guessing-game/data/words.txt") as textFile:
    words = textFile.readlines()
random_word = random.choice(words).strip()

name = input("what is your name? ")
print(f"Good luck! {name}")

print("A 5 letter word has been chosen.")
print("Guess the characters: ")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    
    for char in random_word:
        print("_", end=" ")
        if char in guesses:
            break
        
        
    
    if failed == 0:
        break
    
    print()
    guess = input("Guess a character: ")
    
    guesses += guess
    
    if guess not in random_word:
        break
    
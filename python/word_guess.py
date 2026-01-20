import random

with open("C:/Users/thoma/Projects/word-guessing-game/data/words.txt") as textFile:
    words = textFile.readlines()
random_word = random.choice(words).strip()

name = input("what is your name? ")
print(f"Good luck! {name}")

print("A 5 letter word has been chosen. Use Capitals in order to guess.")
print("Guess the characters: ")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    
    for char in random_word:
        
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed +=1
        
    
    if failed == 0:
        print(f"Congratulations {name}. You win!")
        print(f"The word was {random_word}.")
        break
    
    print()
    guess = input("Guess a character: ")
    
    guesses += guess
    
    if guess not in random_word:
        turns -=1
        print("Wrong!")
        print(f"You have {turns} more guesses.")
        
        if turns == 0:
            print("Oh no! You lost!")
            print(f"The word was {random_word}")
    
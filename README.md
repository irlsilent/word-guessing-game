# Word Guessing Game (Python)

## Description

This project is a simple console-based **word guessing game** written in Python. The program randomly selects a word, and the player must guess the word one letter at a time within a limited number of attempts. After each guess, the game provides feedback indicating whether the guessed letter is in the word and displays the current progress.

The goal of this project is to practice core programming concepts such as input validation, state management, and control flow while building a clean, well-structured beginner-friendly game.

---

## Getting Started

These instructions will help you get a copy of the project running on your local machine for development and testing purposes.

---

## Prerequisites

You will need the following installed:

* **Python 3**

  * Download from: [https://www.python.org/](https://www.python.org/)
  * Verify installation:

    ```
    python --version
    ```

No external libraries are required.

---

## Installing

Follow these steps to run the project locally:

1. **Clone the repository**

   ```
   git clone https://github.com/irlsilent/word-guessing-game.git
   ```

2. **Navigate to the project directory**

   ```
   cd word-guessing-game
   ```

3. **Run the game**

   ```
   python python/word_guess.py
   ```

4. **Play the game**

   * Guess letters one at a time
   * Try to reveal the full word before running out of attempts

---

## How the Game Works

1. A word is randomly selected from a predefined list.
2. The player is shown a masked version of the word using underscores.
3. The player guesses one letter per turn.
4. Correct guesses reveal matching letters in the word.
5. Incorrect guesses reduce the remaining attempts.
6. The game ends when:

   * The word is fully guessed (win), or
   * The player runs out of attempts (loss).

---

## Example Gameplay

```
Word: _ _ _ _ _
Guess a letter: a
Correct!

Word: _ a _ _ _
Guess a letter: z
Incorrect! Attempts remaining: 4
```

---

## Running the Tests

Manual testing example:

1. Start the game
2. Guess valid and invalid letters
3. Verify correct feedback and game behavior

---

## Deployment

This is a local console-based game.

To share or deploy:

* Copy the project folder to another machine with Python installed
* Run the script as described above

---

## Built With

* **Python 3** – Core programming language
* **Standard Library** – Random selection and input handling

---

## Contributing

Contributions are welcome.

You may:

* Open an issue for bugs or suggestions
* Submit pull requests for improvements such as:

  * Replay functionality
  * Difficulty levels
  * Word categories
  * Score tracking

---

## Versioning

This project uses simple versioning.

* **v1.0** – Initial implementation

---

## Authors

* **Thomas Loonis** – Initial work

See GitHub contributors for any additional participants.

---

## License

This project is licensed under the MIT License.
See the `LICENSE.md` file for details.

---

## Acknowledgments

* Inspired by classic word guessing and hangman-style games
* Thanks to online tutorials and documentation that helped reinforce core Python concepts

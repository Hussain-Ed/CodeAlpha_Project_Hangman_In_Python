import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "openai"]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to check if the word is fully guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Main game function
def play_hangman():
    # Select a random word from the list
    word = random.choice(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit on the number of incorrect guesses

    print("Welcome to Hangman!")
    
    # while incorrect_guesses < max_incorrect_guesses and not is_word_guessed(word, guessed_letters):
    while incorrect_guesses < max_incorrect_guesses and  is_word_guessed(word, guessed_letters) != True:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Incorrect guess.")
            guessed_letters.add(guess)
            incorrect_guesses += 1

    if is_word_guessed(word, guessed_letters):
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()

from getpass import getpass

# Display the rules of Hangman
print("Rules of Hangman:\n")
print("You must successfully guess a word or phrase to win the game. You can guess certain letters to help you.")
print("If the letter is in the word/phrase, it will be revealed. If it is not, you lose one life."
      "If you lose all 6 lives, you lose.")
print("Words and phrases cannot include any numbers, but may contain spaces, symbols, etc.")

play = "Y"
while play == "Y":
    # Validate the word
    word = ""
    while not word:
        word = getpass(prompt='Welcome to Hangman! Please enter a word: ', stream=None)
        for letter in word:
            if letter.isnumeric():
                word = ""
                break

    # Create hidden word
    word = word.lower()
    hidden_word = ["_" if x.isalpha() else x for x in word]

    lives = 6
    guesses = []
    while word != "".join(hidden_word):
        print("".join(hidden_word))     # Display Information
        print("Lives remaining:", lives)
        for guess in guesses:
            print(guess)

        guess = input("Guess a letter (If you would like to guess the word, type 'GUESS': ")
        if guess == "GUESS":
            guess = input("Guess the word: ")

            if guess.lower() == word:   # Check word guess
                hidden_word = word
            else:
                lives -= 1
                if lives == 0:
                    break
        else:
            if guess.lower() in word:   # Check letter guess
                oldInd = 0
                for letter in word:
                    if letter == guess.lower():     # Update any guessed letters
                        newInd = word.find(letter, oldInd)
                        hidden_word[newInd] = letter
                        oldInd = newInd+1
            else:
                lives -= 1
                if lives == 0:
                    break
        guesses.append(guess.lower())

    # Final Messages
    if word == "".join(hidden_word):
        print("Congratulations! You guessed the phrase with", lives, " lives remaining.")
    else:
        print("Sorry. You failed to guess the phrase. The phrase was '"+word+"'.")
    play = input("Would you like to play again? Y/N: ")

import random
from WordsList import words


# Dictionary of key:(). Key = incorrect num of guesses
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               
               1: (" o ",
                   "   ",
                   "   "),
               
               2: (" o ",
                   " | ",
                   "   "),
               
               3: (" o ",
                   "/| ",
                   "   "),
               
               4: (" o ",
                   "/|\\",
                   "   "),
               
               5: (" o ",
                   "/|\\",
                   "/  "),
               
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("---- HANGMAN ----")
    for line in hangman_art[wrong_guesses]: # Every line based off of the index of wrong guesses in the hangman art dictionary
        print(line)
    print("-----------------")

def display_hint(hint):
    print(" ".join(hint)) # For each character within our hint, join it by empty space
    print("-----------------")
    

def display_answer(answer):
    print(" ".join(answer)) # For each character within our answer, join it by empty space
    

def main():
    answer = random.choice(words) # Random word from word list
    hint = ["_"] * len(answer) # Creates a list of underscores the same length as the answer
    wrong_guesses = 0 # Counter for incorrect guesses
    guessed_letters = set() # Set to hold the letters that have been guessed, has to use set() bc only () is not allowed
    is_running = True
    
    while is_running:
        display_man(wrong_guesses) # Display man based of number of wrong guesses.
        display_hint(hint) # Display the hint with the letters that have been guessed correctly.
        guess = input("Enter a letter: ").lower() 
        
        if len(guess) != 1 or not guess.isalpha(): # If the length of the guess is not equal to 1 or if the guess is not a letter
            print("Please enter a single letter.")
            continue # Skips loop
        
        # Guessed letter validation
        if guess in guessed_letters: # If the letter has already been guessed
            print("You already guessed that letter.")
            continue # Skips loop
        guessed_letters.add(guess) # Adds the guessed letter to the set of guessed letters
        
        if guess in answer:
            for index in range(len(answer)): # Checks every single index of the answer (every characters)
                if answer[index] == guess: # If the character at the index is equal to the guessed letter
                    hint[index] = guess # Replace the underscore at that index with the guessed letter
        else:
            wrong_guesses += 1 # Increments the number of wrong guesses by 1
            print(f"Wrong guess! You have {6 - wrong_guesses} guesses left.")

        if "_" not in hint: # If no underscores left in hint
            display_man(wrong_guesses) # Display man based of number of wrong guesses.
            display_answer(answer) # Display the answer with the letters that have been guessed correctly.
            print("Congratulations! You guessed the word!")
            is_running = False # Ends the game
        elif wrong_guesses >= len(hangman_art) - 1: # If the number of wrong guesses is greater than or equal to the length of the hangman art dictionary - 1 (bc index starts at 0)
            display_man(wrong_guesses) # Display man based of number of wrong guesses.
            display_answer(answer) # Display the answer with the letters that have been guessed correctly.
            print("Game over! You ran out of guesses.")
            is_running = False # Ends the game

# Ensures that main function is called only when this file is executed
if __name__ == "__main__":
    main()
# Guess the number!

# Module import
import random

# Setting the variables
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num) # Random integer between lowest_num and highest_num
guesses = 0 
is_running = True

# Game introduction
print("-------------------------------")
print("Let's guess a number!!")
print(f"Select a number between {lowest_num} and {highest_num}!!")
print("Type 'q' to quit the game at any time.")
print("-------------------------------")


# While loop to keep game running
while is_running:
    
    # Uses input to see if user puts q in. If not, moves to exception handling
    user_input = input("Enter your guess: ").lower() # Converts input to lowercase for consistency
    if user_input == "q":
        print("Thanks for playing! Goodbye!")
        break
    
    # Exception handling to catch any non-integer input errors
    try:
        guess = int(user_input) # Converts input to integer for comparison
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print(f"Sorry, {guess} is out of range. Please select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("Too low! Try again.")
            print("-------------------------------")
        elif guess > answer:
            print("Too high! Try again.")
            print("-------------------------------")
        if guess == answer:
            print(f"Congratulations! You've guessed the correct number {answer} in {guesses} guesses.")
            is_running = False
        
    except ValueError: # Catches any non-integer input errors
        print("Please enter a valid number.")
        print("Example: 20, 67, 69...")
        print("-------------------------------")
        continue

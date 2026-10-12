#Rock-Paper-Scissors Game
import random

# Declaring starting variables
choices = ["rock", "paper", "scissors"]
is_running = True
score = {"User": 0, "AI": 0}

# Game loop
while is_running:
    user_choice = input("Enter your choice (rock/paper/scissors or 'q' to quit) : ").lower()
    ai_choice = random.choice(choices)
    
    if score["User"] == 3:
        print("Congratulations! You won the game!")
        is_running = False
        break
    elif score["AI"] == 3:
        print("AI won the game! Better luck next time.")
        is_running = False
        break

    if user_choice == 'q':
        is_running = False
        print("Thanks for playing!")
        break

    if user_choice == ai_choice:
        print(f"AI chose {ai_choice}. It's a tie!")
        
    elif user_choice == "rock" and ai_choice == "scissors":
        print(f"AI chose {ai_choice}. You win!")
        score["User"] += 1
    elif user_choice == "rock" and ai_choice == "paper":
        print(f"AI chose {ai_choice}. You lose!")
        score["AI"] += 1
        
    elif user_choice == "paper" and ai_choice == "rock":
        print(f"AI chose {ai_choice}. You win!")
        score["User"] += 1
    elif user_choice == "paper" and ai_choice == "scissors":
        print(f"AI chose {ai_choice}. You lose!")
        score["AI"] += 1
    
    elif user_choice == "scissors" and ai_choice == "paper":
        print(f"AI chose {ai_choice}. You win!")
        score["User"] += 1 
    elif user_choice == "scissors" and ai_choice == "rock":
        print(f"AI chose {ai_choice}. You lose!")
        score["AI"] += 1
    
    else:
        print("Invalid.")
import random

choices = ["rock", "paper", "scissors"]
is_running = True

while is_running:
    user_choice = input("Enter your choice: ").lower()
    ai_choice = random.choice(choices)
    
    if user_choice == ai_choice:
        print(f"AI chose {ai_choice}. It's a tie!")
        
    elif user_choice == "rock" and ai_choice == "scissors":
        print(f"AI chose {ai_choice}. You win!")
    elif user_choice == "rock" and ai_choice == "paper":
        print(f"AI chose {ai_choice}. You lose!")
        
    elif user_choice == "paper" and ai_choice == "rock":
        print(f"AI chose {ai_choice}. You win!")
    elif user_choice == "paper" and ai_choice == "scissors":
        print(f"AI chose {ai_choice}. You lose!")
    
    elif user_choice == "scissors" and ai_choice == "paper":
        print(f"AI chose {ai_choice}. You win!")
    elif user_choice == "scissors" and ai_choice == "rock":
        print(f"AI chose {ai_choice}. You lose!")
    
    else:
        print("Invalid.")
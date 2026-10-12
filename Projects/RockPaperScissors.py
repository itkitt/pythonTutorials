#Rock-Paper-Scissors Game with Cat Cat!
import random

# Declaring starting variables
choices = ["rock", "paper", "scissors"]
win_choices = ["snickered cheekily", "released an evil laughter", "taunted you with his farts"]
lose_choices = ["cried in disbelief", "slammed his paw on the table", "meowed angrily"]
tie_choices = ["looked determined", "is displeased", "puffs his cheeks"]
is_running = True
score = {"User": 0, "Cat Cat": 0}

# Welcome message
print("Welcome to Rock-Paper-Scissors with Cat Cat!")
print("Cat Cat approached and challenged you to a duel of Rock-Paper-Scissors. First to 3 wins!")

# Game loop
while is_running:
    print("----------New Round----------")
    user_choice = input("Enter your choice (rock/paper/scissors or 'q' to quit) : ").lower()
    cat_cat_choice = random.choice(choices)
    cat_cat_win_choices = random.choice(win_choices)
    cat_cat_lose_choices = random.choice(lose_choices)
    cat_cat_tie_choices = random.choice(tie_choices)

    # Check if the user wants to quit
    if user_choice == 'q':
        print("Thanks for playing!")
        print("Cat Cat waved goodbye!")
        break

    # Tie
    if user_choice == cat_cat_choice:
        print(f"Cat Cat chose {cat_cat_choice}. It's a tie!")
        print(f"Cat cat {cat_cat_tie_choices}")
        
    # User - Rock
    elif user_choice == "rock" and cat_cat_choice == "scissors":
        print(f"Cat Cat chose {cat_cat_choice}. You win!")
        print(f"Cat cat {cat_cat_lose_choices} over his loss!")
        score["User"] += 1
    elif user_choice == "rock" and cat_cat_choice == "paper":
        print(f"Cat Cat chose {cat_cat_choice}. You lose!")
        print(f"Cat Cat {cat_cat_win_choices} over his win!")
        score["Cat Cat"] += 1
        
    # User - Paper
    elif user_choice == "paper" and cat_cat_choice == "rock":
        print(f"Cat Cat chose {cat_cat_choice}. You win!")
        print(f"Cat cat {cat_cat_lose_choices} over his loss!")
        score["User"] += 1
    elif user_choice == "paper" and cat_cat_choice == "scissors":
        print(f"Cat Cat chose {cat_cat_choice}. You lose!")
        print(f"Cat Cat {cat_cat_win_choices} over his win!")
        score["Cat Cat"] += 1
    
    # User - Scissors
    elif user_choice == "scissors" and cat_cat_choice == "paper":
        print(f"Cat Cat chose {cat_cat_choice}. You win!")
        print(f"Cat cat {cat_cat_lose_choices} over his loss!")
        score["User"] += 1 
    elif user_choice == "scissors" and cat_cat_choice == "rock":
        print(f"Cat Cat chose {cat_cat_choice}. You lose!")
        print(f"Cat Cat {cat_cat_win_choices} over his win!")
        score["Cat Cat"] += 1
    
    # Invalid input
    else:
        print("Invalid option. Please enter: rock/paper/scissors or 'q' to quit!")
        
    # Displaying the score
    print("----------Current Score----------")
    print(f"User: {score['User']} | Cat Cat: {score['Cat Cat']}")

        
    # Winning condition - breaking the loop 
    if score["User"] == 3:
            print("Congratulations! You won the game!")
            print("Cat Cat cried in defeat, in utter disbelief about his loss. He might have found a newfound respect for you.")
            
            is_running = False
    elif score["Cat Cat"] == 3:
            print("Cat Cat won the game! Better luck next time.")
            print("Cat Cat snickered before releasing a little fart, walking away with a smug look on his face.")
            is_running = False
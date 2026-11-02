# Slot Machine

# Import modules
import random

# Functions

def spin_row():
    # List for symbols
    symbols = ["🍎", "🍉", "🍋", "🔔", "⭐"]
    
    # List comprehension: [criteria, for loop, range]
    return [random.choice(symbols) for _ in range(3)] # "_" is placeholder. Every iteration range 3, return random symbol
    # returns a list because of [] symbols, so row will now be a list.
    
    
    # Essentially what the above code does is:
    # results = []
    # for symbol in range(3):
        # Randomly select a symbol from the list
        # results.append(random.choice(symbols))
    # return results

def print_row(row): # Receives row list as an argument
    print("-------------")
    print(" | ".join(row)) # Uses | as a separator, joins the symbols in the row list
    print("-------------")

def get_payout(row, bet): # Receives row list and bet as arguments
    if row[0] == row[1] == row[2]: # Checks if all symbols in the row are the same, uses [1] and so on to access the second and third symbols in the row list
        if row[0] == "🍎": # If one of them is apple, all of them are due to the if statement above
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0 # If none of the above conditions are met, return 0 payout

# Main program
def main():
    balance = 100 # Default starting balance
    
    # Welcome message and symbols
    print("------------------------------")
    print("Welcome to Cat Cat Slot Machine!")
    print("Symbols: 🍎 🍉 🍋 🔔 ⭐")
    print("------------------------------")
    
    # Game loop
    while balance > 0:
        print(f"Current Balance: ${balance}")
        
        # Bet input
        bet = input("Place your bet amount: ")
        
        # Check if bet is an integer
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue # Skip current iteration and start from beginning
        
        bet = int(bet)
        
        # Check if the bet is greater than the balance
        if bet > balance:
            print("Insufficient funds.")
            continue
        
        # Check if the bet is greater than zero
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        
        # Minus bet from balance,
        balance -= bet
        
        # Initiate the spin. 
        # Row is a list
        row = spin_row()
        print("Spinning... \n")
        print_row(row) # References print_row function, passes the row list as an argument

        # Calculate payout based on the row and bet
        payout = get_payout(row, bet) # References get_payout function, passes the row list and bet as arguments

        # Check if user won or lost
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout # Add payout to balance
        else:
            print("Sorry, you lost this round.")
            
        # Ask user if they want to play again
        play_game = input("Do you want to play again? (y/n): ")
        if play_game.lower() != "y":
            print("------------------------------")
            print(f"Game over. Your final balance is: ${balance}")
            print("Thank you for playing! Goodbye!")
            print("------------------------------")
            break # Exit the loop if user does not want to play again

# Ensures this module is being run directly and not imported
if __name__ == "__main__":
    main()
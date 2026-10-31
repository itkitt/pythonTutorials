# Python Banking Program

# Functions
def show_balance(balance): # Receives balance from main()
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0: # Ensures no negative integers
        print("Please enter a positive number.")
        return 0 # Ensures no errors
    else:
        return amount # To be used in main program's logic

def withdraw(balance): # Receives balance from main()
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance: # Ensures amount is less or equal to balance
        print("Insufficient funds.")
        return 0 # Ensures no errors
    elif amount < 0: # Ensures amount is less or equal to balance
        print("Amount must be greater than 0.")
        return 0 # Ensures no errors
    else:
        return amount # To be used in main program's logic

# Main Program
def main():
    balance = 0 
    is_running = True

    # White loop
    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        # Prompts user to choose choice.
        choice = input("Enter your choice: ")
        
        # Options
        if choice == "1":
            show_balance(balance) # Passes balance to function
        elif choice == "2":
            balance += deposit() # Deposit() works because it returns amount
        elif choice == "3":
            balance -= withdraw(balance) # Withdraw() works because it returns amount
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice.")
    
    # Farewell messages
    print("Thank you for using our Bank Program!")
    print("Have a nice day!")

# Checks if this file is executed
if __name__ == "__main__":
    main()
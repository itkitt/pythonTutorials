# Imports from script1
from script1 import * # Without __name__ = __main__, it would run the entire script1 file

# Functions
def favorite_drink(drink):
    print(f"Your favorite drink is {drink}!")

# Main program
def main():
    print("This is Script 2!")
    favorite_food("Sushi") # If we don't use __name__ == __main__, could conflict with favorite_food("Steak") from script1
    favorite_drink("Tea") 
    print("Goodbye!")

# Checks if this module is executed
if __name__ == "__main__":
    main()
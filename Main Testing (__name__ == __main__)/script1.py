# if __name__ == __main__ : Script can be imported/standalone
# Functions & Classes in this module can be reused without main block of code executing
# Modular, helps readability, leaves no global variables, avoids unintended execution

# Layman: Runs only if this specific file module is executed

# Functions
def greet_name(name):
    print(f"Hello, {name}!")

def favorite_food(food):
    print(f"Your favorite food is {food}!")

# Main program
def main():
    print("Welcome to Script 1!")
    greet_name("Iki")
    favorite_food("Steak")
    print("Goodbye!")

# Ensures that if this is the file running. If we run this file, script1.py = __main__
if __name__ == '__main__':
    main()
# Calculator program

# Turns on calculator
on = True # Boolean variable to control the loop

# Functions
def add(num1, num2):
    result = num1 + num2
    return result # Result is a temporary storage, return throws the value back to the main program, so another variable can catch it (exp: total)

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num2 != 0: # Ensures no error occurs if the user tries to divide by zero
        result = num1 / num2
        return result
    else:
        print("Error: Division by zero is not allowed.") # Exception handling for division by zero
        return None

# Main program logic
while on:
    operator = input("Enter your operator (+, -, *, / or 'q' to quit): ")
    
    # Check if the user wants to quit, or else it'll ask for numbers beforehand
    if operator == "q":
        print("Exiting the calculator. Goodbye!")
        break
        continue # This line is not necessary since break will exit the loop, but it's here for clarity
    
    # Num inputs; put it in loop to prevent infinite results
    num1 = float(input("Enter your first number:  ")) # Sets data type as float
    num2 = float(input("Enter your second number:  "))
    total = 0 # Prevents error if operator is invalid
    
    # If statements
    if operator == "+":
        total = add(num1, num2) # Proves that the variable doesn't have to be the same as the function's temporary storage variable (result)
        print(f"The result is: {total}!") # Output
    elif operator == "-":
        total = subtract(num1, num2)
        print(f"The result is: {total}!") 
    elif operator == "*":
        total = multiply(num1, num2)
        print(f"The result is: {total}!") 
    elif operator == "/":
        total = divide(num1, num2)
        print(f"The result is: {total}!") 
    else: 
        print("Error: Invalid operator. Please use +, -, *, or /.") # Exception handling for invalid operator

# Notes for parameters:
# If function generates own value internally, parameters empty
# If uses outside value, parameters filled with variable names
# Does this function need outside information from the main program to do its math/logic?
# Yes (like add(num1, num2)): Use parameters
# No (it uses input() or fixed values): Leave it empty ().
# Testing Logical Operators (AND, NOT, OR)

# Variables
temperature = float(input("Enter the temperature in Celsius: "))
weather = str(input("Is it raining? (yes/no): ")).lower()
is_raining = True

# Sets rain boolean
if weather == "no":
    is_raining = False
else: 
    is_raining = True

# Check if the event should be cancelled based on temperature and rain (OR Logic Operators)
if temperature > 30 or temperature <0 or is_raining: # Checks if any of these conditions apply
    print("The event has been cancelled")
else: 
    print("The event will proceed as planned")
    
# Additional messages based on temperature and rain (NOT, AND Logic Operators)
if temperature > 35 and not is_raining: # Checks if both conditions are true, negate is_raining condition to opposite
    print("It will be really hot and sunny today, make sure to stay hydrated and wear sunscreen!")
elif temperature < 10 and is_raining:
    print("It will be cold and rainy today, make sure to dress warmly and bring an umbrella!")
else:
    print("The weather is moderate today, enjoy your day!")

# -------------------------------------------

# Membership Operators
# Test if value found within a sequence; IN / NOT IN

# Example 1 - Char in String

secret_word = "travel cat" # String 
letter = input("Guess a letter: ").lower() # Guess character within string

# Implementation
if letter in secret_word:
    print(f"{letter} is found within the secret word!") # If the character is found within secret word
else:
    print(f"{letter} is NOT found within the secret word!")
    

# Example 2 - Value in List

# List & Input declaration 
student_names = {"iki", "damien", "ethan"}
student_name = input("Enter a student name: ").lower()

# Implementation
if student_name not in student_names: # If not within the list
    print(f"{student_name} is not a student!")
else:
    print(f"{student_name} is a student!")

# Example 3 - Dictionary 

# Dictionary & Input declaration
student_grades = {
    "iki" : "A",
    "damien" : "B",
    "ethan" : "C"
}
student_name = input("Enter a student name: ").lower()

# Implementation
if student_name in student_grades:
    print(f"Student {student_name} has a grade of {student_grades.get(student_name)}!") # dictionary[key] gives value ;; or student_grades.get(student_name) // student_grades[student_name]
else:
    print(f"{student_name} is not a student!")
# Match Case Statements (Switch) : Alternative to many "elif" statements
#                                : "match case" case should be a variable

# Case Statement ;; "if-elif-else"
# Format 1
def day_of_week(day_num):
    match day_num:
        case 1:
            return "It is Sunday."
        case 2:
            return "It is Monday."
        case 3:
            return "It is Tuesday."
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday."
        case 5:
            return "It is Friday."
        case 6:
            return "It is Saturday."
        case _: # Wildcard - "else"
            return "Not a valid day."
# Output
print(day_of_week(8))


# Format 2
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday": # Separates values with "|"
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: # Else statement
            return False
# Output
print(is_weekend("Saturday"))

# Implementation

# Input Variable
name = input("What is your name: ").lower()

# Welcome function with match case
def welcome_message(name):
    match name:
        case "iki":
            return "You are my creator, Iki!"
        case "damien":
            return "Hello, Damien!"
        case _:
            return "I do not recognize you..."
# Output
print(welcome_message(name))
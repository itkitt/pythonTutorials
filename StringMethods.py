# String Methods

# User input, variables
name = str(input("Enter your name: "))
name_length = len(name) # Get length of name; starts at 1, counts spaces

# Find first occurrence of character in name
char = str(input("Enter a character to find its position in your name: ")) # Input character to find in name
char_position1 = name.find(char) # Find index position; starts at 0; FIRST OCCURRENCE
char_position1 += 1 # Add 1 to index position to match user input; starts at 1

# Count number of occurrences of character in name
char_count = str(input("Which character would you like to find the occurrences of: ")) # Count number of occurrences of character in name
char_count_result = name.count(char_count) # Count number of occurrences of character in name

# Find last occurrence of character in name
char_position2 = name.rfind(char) # Find index position; starts at 0; LAST OCCURRENCE
char_position2 += 1 # Add 1 to index position to match user input; starts at 1

# Capitalize the name
cap_f_name = name.capitalize() # Capitalize the first letter of the name
upper_name = name.upper() # Convert the name to uppercase
lower_name = name.lower() # Convert the name to lowercase

# Checks if name is all digits or alphabets
is_digit = name.isdigit() # Check if the name is all digits
is_alpha = name.isalpha() # Check if the name is all alphabets

# Replace function
# name = name.replace("k", "g") # Replace all occurrences of "k" with "g" in the name

# Manual
# print(help(str)) # Show all string methods available in Python

# Output
print(f"Your name is {name}, and the length is {name_length}!")
print(f"The character you entered is '{char}', and its first occurrence position in your name is {char_position1}, meanwhile the last occurrence is {char_position2}")
print(f"The character '{char_count}' occurs {char_count_result} times in your name.")
print(f"Your name with the first letter capitalized is: {cap_f_name}, your name in uppercase is: {upper_name}, and your name in lowercase is: {lower_name}.")
print(f"Is your name all digits? {is_digit}! Is your name all alphabets? {is_alpha}!")

# Validate username input from user
# 1. Username != > 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digit

# Verification  rules declaration
print("1. Username must be less than 12 characters \n2. Username must not contain spaces \n3. Username must not contain digits")

# Username validity boolean
username_valid = False

# Check if username is valid based on the rules
while not username_valid: # Loop until username is valid
    username = str(input("Enter your username: ")) # Add name in while loop to prevent infinite loop
    username_length = len(username) # Get length of username; starts at 1, counts spaces
    if username_length > 12: # Check if username is greater than 12 characters
        username_valid = False
        print("Your username is too long, please try again. (Less than 12 characters.)")
        
    elif not username.find(" ") == -1: # Check if username contains spaces, need -1 because find() returns -1 if not found
        username_valid = False
        print("Your username contains spaces, please try again. (No spaces.)")
        
    elif not username.isalpha(): # Check if username contains only alphabets
        username_valid = False
        print("Your username contains digits, please try again. (No digits.)")
        
    else:
        username_valid = True
        break # Exit loop if username is valid

# Outputs validity
print(f"Your username validation turned out: {username_valid}")

# Outputs username if valid
if username_valid:
    print(f"Welcome, {username}!!")
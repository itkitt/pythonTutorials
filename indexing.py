# Indexing ; access element in a sequence using its index ; [start : end : step]
# Start is inclusive, end is exclusive ; step is optional and defaults to 1

# Test variables
var = "123-456-789"
creditnum = "1234-5678-9098-1235"

# Examples
print(var[0])  # Accessing the first character
print(var[4])  # Accessing the fifth character
print(var[-1])  # Accessing the last character
print(var[-7:]) # Accesses the -7 till the end
print(var[:4])  # Accessing the first four characters
print(var[6:])  # Accessing from the seventh character to the end
print(var[4:9]) # Accessing from the fifth character to the tenth
print(var[::2])  # Goes every 2 steps


# Credit card encryption example
lastdigits = creditnum[-4:] 
print(f"Your credit card number is XXXX-XXXX-XXXX-{lastdigits}!")

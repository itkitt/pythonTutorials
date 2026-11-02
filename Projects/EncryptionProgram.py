import random
import string

# List of all characters to be used in encryption 
chars = " " + string.punctuation + string.digits + string.ascii_letters # Imported from string module
chars = list(chars) # Converts the string of characters into a list of characters
# print(chars) to see all the elements (characters) in the list
key = chars.copy()

# Shuffles the key so it is randomized and not in the same order as the original characters
random.shuffle(key) 

# Prints out a reference for which characters are being used in the encryption and what the key is for the encryption
print(f"Chars: {chars}") # Original Letters
print(f"Key: {key}") # Randomized Letters (Encryption Key)
# They follow the same order, so the index of each character in chars corresponds to the index of the encrypted character in key

# ENCRYPT
plain_text = input("Enter the text to be encrypted: ") # User input for the text to be encrypted
cipher_text = "" # Empty string to hold the encrypted text

for letter in plain_text:
    index = chars.index(letter) # Finds the index of the letter we are on
    cipher_text += key[index] # Adds the character of the same index from key into cipher_text, replacing the original character with the encrypted character
    
print(f"Original message: {plain_text}") # Prints out the original message
print(f"Encrypted message: {cipher_text}") # Prints out the encrypted message

# DECRYPT
cipher_text = input("Enter the text to be decrypted: ") # User input for the text to be decrypted
plain_text = "" # Empty string to hold the decrypted text

for letter in cipher_text:
    index = key.index(letter) # Finds the index of the letter we are on
    plain_text += chars[index] # Adds the character of the same index from chars into plain_text, replacing the encrypted character with the original character
    
print(f"Original message: {cipher_text}") # Prints out the encrypted message
print(f"Decrypted message: {plain_text}") # Prints out the decrypted message

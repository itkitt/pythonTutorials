# Testing Module - Random Module
import random

# Setting variables
low = 1
high = 10
options = ["Yes", "No", "Maybe"]
cats = ["Travel Cat", "Bucket Cat", "Drumstick Cat", "Conductor Cat"]

# Testing random integer function
number = random.randint(low, high) # randint is random integer between low and high, inclusive, can't use with strings
print(f"Random number between {low} and {high}: {number}")

# Testing random choice function
decision = random.choice(options)
print(f"Random decision: {decision}")

# Testing shuffle function
random.shuffle(cats)
print(f"Shuffled cat names: {cats}")
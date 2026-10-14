# Functions = Block of reusable code,
#             Place () after the function to invoke it; PARAMETER
#             Values within the parameter() will be used; ARGUMENT


# Creating the function
def happy_birthday(name, age):
    print(f"Happy birthday, {name}!! You are {age} years old!")

# Input for the arguments
name = input("What is your name: ")
age = input("What is your age: ")

# Testing out the function with input arguments
happy_birthday(name, age) # order of the arguments matter
happy_birthday("Travel Cat", 2)


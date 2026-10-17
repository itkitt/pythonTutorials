# Default Argument: Default value for certain parameters
#                 : Used when argument is omitted, makes func more flexible, reduces # of arguments ;; 1. position, 2. DEFAULT, 3. keyword, 4. arbitrary

# Module for counter project
import time

# ------ DEFAULT ARGUMENT -------

# Calculate net price
def net_price(list_price, discount=0, tax=0.05): # DEFAULT discount is 0, tax is 5%
    return list_price * (1 - discount) * (1 + tax)

# Implementation
print(net_price(500)) # list_price = 500, with discount and tax being DEFAULT
print(net_price(500, 0.1, 0)) # Changing default arguments, discount = 0.1 (1%) and tax = 0%

# Counter project
def count(end, start=0): # Input parameters have to go first. Default value for start = 0
    for x in range(start, end+1): # Changing order so start is the first to go. Range excludes last number, so add 1 to default to be accurate
        print(x)
        time.sleep(1)
    print("Done!")

# Counter usage
count(1)

# -----------

# ------ KEYWORD ARGUMENT -------
# Use positional argument first (first position) and others can be keyword arguments
# "end=','" is a keyword argument

# Greeting function
def greeting(greet, title, firstname, lastname):
    print(f"{greet}, {title}{firstname} {lastname}")
    
greeting("Hi",firstname="Iki", lastname="Cheng", title="Mr.") # Uses "hi" as first position argument, and the rest are keyword arguments

# -----------

# ------ ARBITRARY ARGUMENT -------
# *args     = Pass multiple non-key arguments
# **kwargs  = Pass multiple key arguments
# *         = Unpack operator

# Testing *args
def add(*args): # Allows you to add as many arguments, *args can be changed to *numbers or any names ;; Changes into tuple
    total = 0
    for n in args:
        total += n
    return total
    
# Implementation
print(add(1,2,3)) # Adds as many as you want

# Testing **kwargs
def address(**kwargs): # Allows adding keyword arguments, changes into dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Implementation
address(room = "4-09",
        apartment = "Cat Lounge",
        city = "Nyanbare Hill",
        country = "Cat Cat Land")

# Project using *args and **kwargs
def shipping_address(*args, **kwargs): # *args must come first before **kwargs to else it'll have a syntax error
    for arg in args:
        print(arg, end=" ")
    print()
    
    print(f"{kwargs.get('room')}, {kwargs.get('apartment')}")
    print(f"{kwargs.get('city')}, {kwargs.get('country')}")
    
shipping_address("Iki", "Cheng",
                 room = 3,
                 apartment = "Travel Cat Hotel",
                 city = "Cat Valley",
                 country = "Cat Cat Land")
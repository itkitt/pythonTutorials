# Default Argument: Default value for certain parameters
#                 : Used when argument is omitted, makes func more flexible, reduces # of arguments ;; 1. position, 2. DEFAULT, 3. keyword, 4. arbitrary

# Module for counter project
import time

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
count(10)
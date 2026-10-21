# Collection = Single "variable" used to store multiple values
# List  [] = Ordered, changeable. Duplicates.
# Set   {} = Unordered, immutable, can add/remove. No duplicates.
# Tuple () = Ordered and unchangeable. Duplicates. Fast.

# Variables
fruits = ["Apple", "Banana", "Grapes", "Orange"]
# fruits[0] = "Guava"           -- Replaces first element to Guava
# fruits.append("Tomato")       -- Adds new element "Tomato"
# fruits.remove("Banana")       -- Removes banana as an element
# fruits.insert(0, "Pineapple") -- Adds pineapple as first element, original first element becomes second
# fruits.sort()                 -- Sorts in alphabetical
# fruits.clear()                -- Clears all elements
# fruits.index("Grapes")        -- Finds index of stated element
# fruits.count("Orange")        -- Counts how many oranges are in fruits list

# Testing inputs to append into list
extra_fruit = input("Please enter a fruit name: ")
fruits.append(extra_fruit)

# Access elements within List
print(fruits[1]) # Prints element located in index 1
print("Apple" in fruits) # Checks existence

for fruit in fruits:
    print(fruit, end = " ") # Prints through for loop, accessing and outputting each elements
    
print() # To break outputs
    
# print(help(fruits)) or print(dir(fruits)) -- Shows and explains all functions within lists

# -----------
# List Comprehension : Concise way to create lists
#                    : [{expression} for {value} in {iterable} if {condition}]

# Creates a list that multiplies value with 2 for 10 times
doubles = [x*2 for x in range(1,11)] # x*2 = expression, x = value, range(1,11) = iterable
print(doubles)

# Creates a list that multiplies value with 3
triples = [y*2 for y in range(1,11)] 
print(triples)

# Squares each values
squares = [z*z for z in range(1,11)] 
print(squares)

# Integrating if statements

# Number List
numbers = [1, -2, 3, -4, 5, -6, 8, -7, -9, 10, 6, -14]

# Implementations
positive_nums = [num for num in numbers if num >= 0] 
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print (positive_nums)
print (negative_nums)
print (even_nums)
print (odd_nums)

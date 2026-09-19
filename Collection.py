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
    
# print(help(fruits)) or print(dir(fruits)) -- Shows and explains all functions within lists




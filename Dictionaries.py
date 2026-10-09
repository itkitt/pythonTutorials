# Dictionaries
# {key:value} pairs. Ordered, changeable, no duplicates.
# Exp: {id:name}, {item:price}, {country:capital}

# Setting the values
capitals = {"Malaysia": "Kuala Lumpur",
            "Japan": "Tokyo",
            "France": "Paris",
            "Germany": "Berlin",
            "Italy": "Rome"}

# Usage
print(capitals.get("Malaysia")) # Gets the value of the key "Malaysia"

# Checks if key is within dictionary
if capitals.get("Malaysia"): # If not empty
    print("That capital exists")
else: # If empty
    print("That capital does not exist")
    
# Update function
capitals.update({"England": "London"}) # Adds new key:value pair into dictionary, or replace existing keys

# Remove function
## capitals.pop("Germany") <---- # Removes key:value pair from dictionary
## capitals.popitem() <---- # Removes last key:value pair from dictionary
## capitals.clear() <---- # Clears all key:value pairs from dictionary

# Only find the keys
key = capitals.keys() # Returns all keys in dictionary
#print(key) 
for key in capitals.keys():
    print(key, end = ", ")

# Only find the values
value = capitals.values() # Returns all values in dictionary
#print(value)
for value in capitals.values(): # Easier to read
    print(value, end = ", ")
    
# items
items = capitals.items() # Returns all key:value pairs in dictionary
#print(items)
for item in capitals.items(): # Easier to read
    print(item, end = ", ") # 2D Tuple lists 
    
# Easiest form to read:
for key, value in capitals.items():
    print(f"{key}: {value}")

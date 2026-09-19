# Shopping Cart!

# Boolean for turning on the app
app_on = True

# Creates the lists
foods = []
necessities = []
food_prices = []
necessities_prices = []
total = 0

# Containers (def)
def food_list():
    food = str(input("Please enter a food item: "))
    foods.append(food)
    food_price = float(input("How much is this food item: $"))
    food_prices.append(food_price)
    
def necessities_list():
    necessity = str(input("Please enter a necessity: "))
    necessities.append(necessity)
    necessities_price = float(input("How much is this necessity: $"))
    necessities_prices.append(necessities_price)

# Main program
while app_on:
    navigation = input("Would you like to insert a food item (f), a necessity (n) or quit (q): ")
    if navigation.lower() == "f":
        food_list()
    elif navigation.lower() == "n":
        necessities_list()
    elif navigation.lower() == "q":
        break
    else:
        print("Error occurred, no such commands found.")

# Calculations
for food_price in food_prices:
    total += sum(food_prices)
    
for necessity_price in necessities_prices:
    total += sum(necessities_prices)

# Outputs
print("----- Food -----")
for food in foods:
    print(food, end="\n")
    
print("----- Necessities -----")
for necessity in necessities:
    print(necessity, end="\n")
    
print("----- Total -----")
print(total)
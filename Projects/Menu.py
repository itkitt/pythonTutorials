# Concession stand
# Utilizes dictionary

# Constructing and defining the menu items. {key: value} = {item: price}
menu = {"mala mushrooms": 2.99,
        "mala boiled fish": 19.99,
        "chinese roasted pork": 40.30,
        "lamb skewers": 6.99,
        "chicken skewers": 5.99,
        "pork skewers": 5.99,
        "beef skewers": 6.99,
        "lanzhou beef noodles": 12.99,
        "fried rice": 8.99,
        "chinese tea": 2.00,
        "white rice": 2.00}

# Declaring parameters for the order
cart = {}
total = 0

# Menu display!
print("Welcome to Neko Lounge's Chinese Restaurant!")
print("---------- M E N U ----------")

# Displays the contents 
# item = key, price = value ; this is what we wanna call it!
for item, price in menu.items():
    print(f"{item:20}: RM {price:.2f}") # Formats item with 20 spaces and price with 2 decimal places

print("------------------------------") # Closes the menu display
    
# Lets user picks items in menu
while True: 
    food = input("What would you like to order? (Type 'q' when finished): ").lower() # Converts input to lowercase for consistency
    
    if food == "q":
        break
    
    elif menu.get(food) is not None: # Checks if the food item is in the menu
        try:
            quantity = int(input(f"How many {food} would you like to order: ")) # Asks for quantity of the food item
            if quantity <= 0: # Checks if the quantity is a positive number
                print("Please enter a positive number for the quantity.")
                continue
        except ValueError: # Catches any non-integer input errors
            print("Invalid input. Please enter a valid number for the quantity.")
            continue
        cart[food] = cart.get(food, 0) + quantity # Adds the food item and quantity to the cart
        total += menu[food] * quantity # Updates the total price
        print(f"{quantity}x {food} added to your order. Current total: RM {total:.2f}")
        
        
    else: # Catches any other input errors
        print("Invalid input. Please try again.")
    
# Order display!
print("---------- O R D E R ----------")

# Outputs the final order and total
for food, quantity in cart.items():
    item_total = menu[food] * quantity # Calculates the total price for each item
    print(f"{quantity}x {food:17}: RM {item_total:.2f}") # Formats item with 20 spaces and price with 2 decimal places
print(f"Total               : RM {total:.2f}") # Displays the total price of the order
print("------------------------------") # Closes the order display




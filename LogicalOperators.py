# Testing Logical Operators (AND, NOT, OR)

# Variables
temperature = float(input("Enter the temperature in Celsius: "))
weather = str(input("Is it raining? (yes/no): ")).lower()
is_raining = True

# Sets rain boolean
if weather == "no":
    is_raining = False
else: 
    is_raining = True

# Check if the event should be cancelled based on temperature and rain (OR Logic Operators)
if temperature > 30 or temperature <0 or is_raining: # Checks if any of these conditions apply
    print("The event has been cancelled")
else: 
    print("The event will proceed as planned")
    
# Additional messages based on temperature and rain (NOT, AND Logic Operators)
if temperature > 35 and not is_raining: # Checks if both conditions are true, negate is_raining condition to opposite
    print("It will be really hot and sunny today, make sure to stay hydrated and wear sunscreen!")
elif temperature < 10 and is_raining:
    print("It will be cold and rainy today, make sure to dress warmly and bring an umbrella!")
else:
    print("The weather is moderate today, enjoy your day!")
    

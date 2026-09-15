# {value:flags} format a value based on the flags

# Translations:
# .2f = 2 decimals, float
# :10 = 10 spaces to display output
# :010 = 10 spaces, 0 replaces empty spaces
# :<10 = Left justify, 10 spaces
# :^10 = Centralize
# :+ = Show positive or negative
# :, = Thousand separator

# Variables
price1 = 3.14593
price2 = -98.765
price3 = 12.34
price4 = 239485.20385

# Examples
print(f"Price 1 is ${price1:.2f}") #.2 = 2 decimals, f = float
print(f"Price 2 is ${price1:10}") # 10 spaces to display output
print(f"Price 3 is ${price1:010}") # 10 spaces to display output, 0 will replace empty spaces
print(f"Price 1 is ${price1:<10}") # Left justified, so spaces will be at the right
print(f"Price 2 is ${price2:^10}") # Centralize
print(f"Prices are is, ${price1:+}, ${price2:+} and ${price3:+}") # Display positive/neg
print(f"Price 4 is ${price4:,.2f}") # Thousand separator, 2 decimals float
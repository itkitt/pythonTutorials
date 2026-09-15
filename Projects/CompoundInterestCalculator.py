# Computer interest calculator
# Uses pow function, while loops, if statements, format specifier

# Variables
principle = 0
interest_rate = 0
time = 0

# Functions
while principle == 0: # While principle is 0
    principle = float(input("Enter your principle amount: ")) # Inputs principle as float
    if principle <= 0: # If principle is still less than or equal to 0
        print("Principle can't be less than or equal to 0.") # Error message

while interest_rate == 0:
    interest_rate = float(input("Enter your interest rate: "))
    if interest_rate <0:
        print("Interest rate cannot be less than or equal to 0.")
        
while time == 0:
    time = int(input("Enter the time in years: ")) # Int because year
    if principle <= 0:
        print("Years can't be less than or equal to 0.")
        
total = principle * pow((1 + interest_rate / 100), time) # Compound interest formula; principle x (1 + interest/100)^time

# Output
print(f"Your principle is ${principle:.2f}\nYour interest rate is {interest_rate:.2f}%\nYour time in years is {time}")
print(f"With principle (${principle:.2f}) multiplied by 1 + interest rate ({interest_rate:.2f}%), with the power of years ({time})...")
print(f"Your compound interest would be: ${total:.2f}")
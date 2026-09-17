# Countdown Timer 
# Uses time module, for loop, modulo, format specifier

# Dependencies 
import time 

# Inputs
my_time = int(input("Please enter the time in seconds: "))

# Main program
for x in range(my_time, 0, -1): # Starts at my_time, ends at 0, -1 step = goes backwards
    seconds = x % 60 
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # Specified format: 0 = fill spaces with "0", 2 Width of text = 2
    time.sleep(1) # Stops per second
    
print("TIME'S UP!") # Informs user that the time has reached

# "%" - modulo: Calculates remainder
#       x = 65 seconds, 65 % 60 leaves a remainder of 5. The extra 60 seconds are absorbed into the minutes column, leaving w leftover seconds.


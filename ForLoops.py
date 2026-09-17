# For Loops : Execute code a fixed num of time; iterate over range, sequence, string, etc
# Format: for x in range(begin, end, steps)
#         "x" can be named anything

# Example 1 - Typical implementation
for x in range(1, 11, 2): # Counts from 1 to 10, beginning inclusive, end exclusive, steps
    print(x) # Shows all the steps taken
    
# Example 2 - Countdown to birthday
for counter in reversed(range(1, 11)): # Reverse the output, 10 to 1
    print(counter)
print("Happy Birthday!")

# Example 3 - Outputs each individual elements
variable = "It will print step by step."
for var in variable: 
    print(var) # It will print each of the character step-by-step.
    
# Example 4 - Skip an element
for y in range(1, 20):
    if y == 4 or y == 14: # Skips these elements, OR func requires retype of "y"
        continue # Skips over declared elements
    else:
        print(y)
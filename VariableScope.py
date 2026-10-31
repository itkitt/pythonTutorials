# Variable Scope            : Where a variable is visible/accessible 
# Scope Resolution ; (LEGB) : Local -> Enclosed -> Global -> Built-in
#                           : Priority order! If local can't be found, use enclosed, etc etc

# Local
# Declared variables within a function could only be used within the function; They are local variables
# Functions can't see inside of other functions, hence why we have to pass other arguments into functions, func1(x,y)
def func1():
    a = 1 # Declares "a = 1" only in this function
    print(a)
    
def func2():
    a = 2 # In this function, a = 2, compared to in func1
    print(a)

# Output
func1()
func2()

# Enclosed
# If functions are written inside another, the declared variable in the main function (func3) will be used by nested function (func4) if no variables are declared in nested function.

def func3():
    x = 5
    def func4():
        # x = 6 // If this is included, x = 6. If not, it will use enclosed variable of func3 : "x = 5"
        print(x)
    func4()

# Output
func3()

# Global
# Variables outside of any functions

# Global variable declared outside of any functions, can be used by all.
x = 10

def func5():
    print(x) # Uses the global function "x = 10"

# Output
func5()

# Built-in
# The variables from modules

# Module import
from math import e

# Function
def func6():
    print(e) # Will output the variable imported from math module. If there were any variables (global/enclosed/etc) with the same name it will used those first.
    
# Output
func6()
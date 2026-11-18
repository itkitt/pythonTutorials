# Exception = Event that interrupts the flow of program ; ERROR
#             ZeroDivisionError = Dividing by 0 (20/0), TypeError = Operation with wrong data type (1 + "1"), ValueError = Typecasting data wrongly (int("pizza"))
# Steps     = 1. try, 2. except, 3. finally

# First step
try:
    number = int(input("Enter a number: "))
    print(1/number)
    
# Chaining the except blocks
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Enter only numbers.")
except Exception: # Catches all exceptions - Last Resort
    print("Something went wrong!")
    
# Always executes no matter what
finally:
    print("Do some cleanup here!")
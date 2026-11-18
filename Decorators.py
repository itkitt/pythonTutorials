# Decorator = Function extending the behaviour of another function
#           = w/o modifying the base function
#           Pass the base function as an argument to the decorator

#           @add_sprinkles
#           get_ice_cream("vanilla")
#           ^^ Adds sprinkles to one vanilla ice cream instead of ALL vanilla ice cream

# Extending the initial function
def add_sprinkles(func):
    def wrapper(*args, **kwargs): # Prevents auto-run, accepts all arguments
        print("*Adds sprinkles 🎊*")
        func(*args, **kwargs) # References initial function
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs): # Prevents auto-run
        print("*Adds fudge 🍫*")
        func(*args, **kwargs)
    return wrapper

# Initial function
@add_sprinkles # Initiates the extension to add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")
    
get_ice_cream("vanilla")
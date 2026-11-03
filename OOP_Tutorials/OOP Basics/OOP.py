# Object = Bundle of related attributes (variables) and methods (functions)
#        = Ex. Phone, Cup, Book
#        = Each of these objects can have different attributes to represent it.
#        = Such as version_num, is_on, price, title, pages, etc
#        = Methods could be like: open_book(), close_book(), actions

#        = Need a "class" to create many objects
# Class  = BLUEPRINT used to design the structure/layout of an object

# Making the constructor in another script, import it here
from car import Car
        
CatCatCar = Car("Subaru", 2003, "Blue", False) # Self is already provided in the background
# print(CatCatCar) # Gives memory address instead
print(F"Cat Cat's car is a {CatCatCar.model} and is it for sale? : {CatCatCar.for_sale}") # "." = Attribute access operator

IkiCar = Car("Tesla", 2026, "White", False)
NewCar = Car("Proton", 2026, "Red", True)

print(f"Iki's car is made in {IkiCar.year}!")
print(f"Is new car for sale? : {NewCar.for_sale}")


# Method tests
IkiCar.drive() # The same output for all the objects within this class.
CatCatCar.stop()
NewCar.describe()
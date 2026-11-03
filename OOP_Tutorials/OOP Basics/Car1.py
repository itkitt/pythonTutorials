# Object = Bundle of related attributes (variables) and methods (functions)
#        = Ex. Phone, Cup, Book
#        = Each of these objects can have different attributes to represent it.
#        = Such as version_num, is_on, price, title, pages, etc
#        = Methods could be like: open_book(), close_book(), actions

#        = Need a "class" to create many objects
# Class  = BLUEPRINT used to design the structure/layout of an object

class Car:
    
    # Class Variables : Defined outside constructor, shares data (instances) among all objects created from that class
    wheels : 4
    
    # Constructor method
    def __init__ (self, model, year, colour, for_sale): # __init__ is initialize, self is "this object we're creating now", the other attributes are what is within "PARAMETERS"
        self.model = model # When receiving a model name, assigns it to this object "self.model"
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
        
    # Method
    def drive(self): # Self = "object we're currently working with"
        print(f"You drive the {self.colour} {self.model}.") # Allows for referencing, when you do IkiCar.drive() would give IkiCar's model
        
    def stop(self):
        print(f"You stopped the car {self.colour} {self.model}.")
        
    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")
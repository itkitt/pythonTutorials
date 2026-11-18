# Static Method = Method belong to a class rather than any object from that class (instance)
#               = Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects); Methods belong to individual objects from that class -- For OBJECTS
# Static methods = Best for utility functions that do not need access to class data -- For OUTSIDE DATA, no access to class data
# Class methods = Best for class-level data / require access to class -- For CLASS DATA

# Class declaration
class Employee:
    
    # Constructor
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    # Instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    # Static method - General utility that can be used anywhere
    @staticmethod
    def is_valid_position(position): # Don't have self as argument cause not working with objects created from this class
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"] # All available positions
        return position in valid_positions # Check if position is within valid_positions list
    
# Initiate static method
print(Employee.is_valid_position("Cook")) # Uses the method, argument is the position you wanna check
print(Employee.is_valid_position("Scientist"))

# Constructing the instances
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# Instance methods, have to be used with objects
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
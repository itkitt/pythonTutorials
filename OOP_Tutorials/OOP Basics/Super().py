# super() = Function used in child class to call methods from parent class (superclass)
#           Allows to extend functionality of the inherited method


# Parent
class Shape:
    def __init__(self, color, is_filled): # Constructor
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# Child
class Circle(Shape):
    def __init__(self, color, is_filled, radius): # Overwrites the initial __init__ from parent class, so super() is needed to reference
        super().__init__(color, is_filled) # Uses super().__init__() to reference the initial parent's constructor (__init__)
        self.radius = radius # New attribute unique to this child class

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2") # Method overwriting; child's method with be used if called
        super().describe() # The describe method in parent class will also be used when described is called, along with the describe method in the child class


class Square(Shape): 
    def __init__(self, color, is_filled, width):
        self.color = color
        super().__init__(color, is_filled) # Uses super().__init__() to reference the initial parent's constructor (__init__)
        self.width = width
        
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm*2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        self.color = color
        super().__init__(color, is_filled) # Uses super().__init__() to reference the initial parent's constructor (__init__)
        self.width = width
        self.height = height
        
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()
        
# Declarations
circle = Circle("red", True, 5) # Circle(color="red", is_filled=True, radius=5)
square = Square("blue", False, 6)
triangle = Triangle("pink", True, 5, 3)

# Method testing

#print(circle.color, circle.is_filled, circle.radius)
#print(triangle.width, triangle.height)
#print(square.color)
circle.describe() # Should give unique describe method output + parent class describe method output
square.describe()
triangle.describe()


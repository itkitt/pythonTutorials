# @property = Decorator used to define a method as property (It can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives getter / setter / deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width # Makes data private, cannot be accessed unless using setter/getting, _width
        self._height = height # Makes data private, cannot be accessed unless using setter/getting, _height -- USED INTERNALLY
        
    # Getter Methods - Gets data
    @property # When printing 'rectangle.width and so on, will return from here
    def width(self):
        return f"{self._width:.1f}cm"
        
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    # Setter Methods - Set/Write
    @width.setter 
    def width(self, new_width): # Don't use same variable name as the original variable
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater than zero.")
            
    @height.setter 
    def height(self, new_height): # Don't use same variable name as the original variable
        if new_height >0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")
            
    # Deleter Method - Clears data
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted.")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted.")

rectangle = Rectangle(3, 4)

# Initializes the Setter Methods - Overrides rectangle width/height
rectangle.width = 6
rectangle.height = 7

# Initializes Delete Methods 
# del rectangle.width
# del rectangle.height

# Initializes the Getter Methods
print(rectangle.width)
print(rectangle.height)


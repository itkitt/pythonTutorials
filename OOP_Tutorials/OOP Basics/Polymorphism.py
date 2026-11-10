# Polymorphism = Greek word "have many forms/faces"
#    Poly      = Many
#    Morph     = Form

# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1.  Inheritance   = An object could be treated of the same type as a parent class
# 2. "Duck Typing"  = Object must have necessary attributes/methods
#                   = "If it looks like a duck + quacks like a duck, it must be a duck."


# Import abstract method
from abc import ABC, abstractmethod

# Parent class
class Shape1: 
    
    @abstractmethod
    def area(self):
        pass

# Child class
class Circle(Shape1):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2 

class Square(Shape1):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
class Triangle(Shape1):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

# Square = Square() # Forms: 1. Square, 2. Shape1 ;; Derived from Shape1 class and Circle class
# Pizza = Pizza() # Forms: 1. Pizza, 2. Square, 3. Shape ;; Drived from parent class and "grandparent" class

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm2")
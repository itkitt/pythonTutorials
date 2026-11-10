# 2. "Duck Typing"  = Object must have necessary attributes/methods
#                   = "If it looks like a duck + quacks like a duck, it must be a duck."

# Parent Class
class Animal:
    alive = True

# Child Class
class Dog(Animal):
    def speak(self):
        print("WOOF")
        
class Cat(Animal):
    def speak(self):
        print("MEOW")
        
class Car:
    def horn(self):
        print("HONK")

# List declaration
animals = [Dog(), Cat()] 
# animals = [Dog(), Cat(), Car()] 
# ^^ output would be "car have no attribute: speak, bc it doesn't share the same attribute, same for alive attribute"

# Output test
for animal in animals:
    animal.speak()
    print(animal.alive) 
# These are able to have an output because they share the same necessary attribute/methods
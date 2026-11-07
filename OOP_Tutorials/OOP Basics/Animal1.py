# Inheritance = Class inherit attributes + methods from another class (superclass)
#               Helps with reusability and extensibility 
#               class Child(Parent)

# Parent Class (Superclass)
class Animal:
    def __init__(self, name,):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating...")
        
    def sleep(self):
        print(f"{self.name} is sleeping...")
        

# Child Class
# Child classes can have functions/methods unique to them
class Dog(Animal):
    def speak(self):
        print(f"{self.name} said: 'Woof!'") # Unique method 

class Cat(Animal):
    def speak(self):
        print(f"{self.name} said: 'Meow!'")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} said: 'Squeeek!'")

dog = Dog("Bluey")
cat = Cat("Travel Cat")
mouse = Mouse("Mickey")

dog.speak()
cat.speak()
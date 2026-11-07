# Multiple inheritance   = inherit from 1+ parent class
#                          C(A, B)

# Multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

# Parents (1)
class Animal1:
    def __init__(self, species): # Only need one initialize bc this is the "first parent", everyone inherits from animal class
        self.species = species
        
    def eat(self):
        print(f"This {self.species} is eating.")
        
    def sleep(self):
        print(f"This {self.species} is sleeping.")


# Parents (2) / Children of Parents(1)
class Prey(Animal1):      
    def flee(self):
        print(f"This {self.species} is fleeing") # Uses self.species from Animal1

class Predator(Animal1):
    def hunt(self):
        print(f"This {self.species} is hunting.")

# Child
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # Inherits from both classes
    pass

# Declarations
rabbit = Rabbit("rabbit") # Species declaration
hawk = Hawk("hawk")
fish = Fish("fish")

# Method tests
rabbit.flee() # Rabbit has flee method but not hunt method
hawk.hunt() # Hawk has hunt method and no flee method

# Fish has both hunt and flee because it inherited it from both Prey & Predator parent classes
fish.flee()
fish.hunt()
fish.sleep()
# Class name
class Student:
    
    # Class Variable
    class_year = 2024 # Every objects shares this variable
    num_students = 0 
    
    # Initialize 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        Student.num_students += 1 # Uses class variable by using class name (Student) and the class variable

# Class methods = Allow operations related to the class itself
#               = Take (cls) as the first parameter, which represents the class itself, instead of (self)

# Instance methods = Takes (self) as the first parameter

# Class declaration
class Student:
    
    # Class variable
    count = 0
    total_gpa = 0
    
    # Constructor
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # Increments class variable by 1
        Student.total_gpa += gpa 
        
        
    # Instance Method
    def get_info(self):
        return f"{self.name}, {self.gpa}"
        
    @classmethod
    def get_count(cls): # Uses class parameter
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}" # Average is total_gpa divided by total count of students, formats results to 2 decimal

# Creating instances
student1 = Student("Iki", 4) 
student2 = Student("Ethan", 3)
student3 = Student("Damien", 3.5)

# Using the class method
print(Student.get_count())
print(Student.get_average_gpa())
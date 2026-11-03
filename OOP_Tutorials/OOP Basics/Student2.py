from Student1 import Student

# Object Creation
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Travel Cat", 2)
student4 = Student("Mr Fox Fox", 1)

print(student1.name, student1.age, student1.class_year)
print(Student.class_year) # Standard practice for readability

print(f"My graduating class of {Student.class_year} has {Student.num_students} students!")
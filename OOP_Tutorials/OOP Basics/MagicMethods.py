# Magic Methods = Dunder methods (double underscore): __init__, __str__, __eq__, __lt__
#               = Called by Python's built-in operations
#               = Allow developers to define/customize behaviour of objects

# Class Declaration
class Book:
    
    # Constructor
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    # When creating instances/objects, automatically calls __init__
    
    # String method
    def __str__(self):
        return f"'{self.title}' by {self.author}" # Prints this when printing an object, instead of memory location
    
    # Equal method
    def __eq__(self, other): # Other is the other object to be compared
        return self.title == other.title and self.author == other.author
    
    # Less than method
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    # Greater than method
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    # Addition
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    # "in" method
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    # Get function
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was no found"
    
# Uses __init__ constructor to build instances
book1 = Book("Pride and Prejudice", "Jane Austen", 300)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("Great Expectations", "Charles Dickens", 280)
book4 = Book("Pride and Prejudice", "Jane Austen", 300) 

# Returns string with __str__ ; representation of object when printed
print(book1)

# Print if equal with __eq__
print(book1 == book4)

# Compares if have less pages / greater than - __lt__ / __gt__
print(book2 > book3)

# Page_num addition, __add__
print(book1 + book2)

# If a certain word is in title/author
print("Pride" in book1)
print("Cat" in book2)
print("Austen" in book4)

# Get function
print(book3["title"])
print(book3["author"])
print(book3["num_pages"])
print(book3["audio"])
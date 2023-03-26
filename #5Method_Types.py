class Student:
    school = "Numl"
    def __init__(self,marks1,marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def avg(self):    # Instance Method b/c we are passing self it means it belongs to particular object we are defining it in class but it works with objects
        return (self.marks1 + self.marks2 + self.marks3)/3
    """
     Instance Method has 2 types:
     1. Accessor Method (Getter)
     2. Mutator Method (Setter)
    """
    def get_marks1(self):      # Accessor
        return self.marks1
    
    def set_marks1(self,value): # Mutator
        self.marks1 = value
        
        
###### If We want to work with Class variable we need Class Method ########
    @classmethod    # Decorator
    def getSchoolName(cls):    # Class method here we can pass Class
        return cls.school
        
###### Method which has nothing to do with Class & Instance variable we use static Method ########
    ### Helpful for finding operation which helps others methods / Variables i.e Something Extra ###
    @staticmethod
    def info():  # Static method no argument passing
        print("This is Student Class Static Method")
s1 = Student(23,57,89)
s2 = Student(55,67,22)

print(s1.avg())  # Here we are passing instance i.e s1 not Class name
print(s2.avg())

print(Student.getSchoolName())  # calling Class Method

Student.info() # Calling Static Method



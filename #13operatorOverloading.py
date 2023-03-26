a = 6
b = 5

print(a+b) # Behind the scenes '+' operator call (.__add__(a,b)) method (Magic Method)
print(int.__add__(a,b))

"""
In operator(+, -, *, /) Overloading operator will remain same but the operand will change
means the type of parameter we are passing will change.
i.e __add__() method takes different types of arguments/parameters that is Overloading.
Overloading means same method name but the argument are different i.e no. of arguments / type of arguments. 
"""

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self, other):     # Overload the Ooperator of '+'
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    
    def __str__(self):                  # Overriding the method
        return f'{self.m1}, {self.m2}'  # Convert to String b/c by default when we say print() we want to print a String   
    
s1 = Student(20, 65)
s2 = Student(40, 15)

s3 = s1 + s2     # behind -> Student.__add__(s1, s2)
print(s3.m1)
print(s3.m2)

print(a)   # Behind the scenes it is calling 'a.__str__()'  
print(s1)  # Behind the scenes it is calling 's1.__str__()' defind in class by overriding the buit-in '.__str()' method  

class A:               # Parent Class / Super Class
    def __init__(self):
        print("In A __init__")
    
    def feature1(self):
        print("Feature 1 Working")
        
    def feature2(self):
        print("Feature 2 Working")

class B(A):               # Child Class / Sub Class of Parent Class "A" Now we can also use/access A Class function in B Class
    def __init__(self):
        super().__init__()   # It will call _init_ of Super Class A
        print("In B __init__")
        
    def feature3(self):
        print("Feature 3 Working")  
        

# obj1 = A()
obj2 = B() # If we haven't defined the Constructor of B it will call the Constructor of A otherwise it will call its own Constructor


"""
If we Create object of Sub Class it will first try find _init_ of of Sub Class. If 
it is not found then it will call _init_ of Super Class

Super(Keyword):-
Using Super we can access all the features of Parent Class in Sub Class.

When we create object of sub class it will call _init_ of sub class first if we have
call super then it will first call _init_ of Super Class then _init_ of Sub Class

"""
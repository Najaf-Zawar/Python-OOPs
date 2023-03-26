class A:              
    def __init__(self):
        print("In A __init__")
    
    def feature1(self):
        print("Feature 1-A Working")
        
    def feature2(self):
        print("Feature 2 Working")

class B:               
    def __init__(self):  
        print("In B __init__")
     
    def feature1(self):          # Same feature name as A class
        print("Feature 1-B Working")   
               
    def feature3(self):
        print("Feature 3 Working") 

class C(A,B):  # Inherit from (Sub Class of) Class A & B 
    def __init__(self):
        super().__init__() # Here We have two Parent Classes but it will Call the Constructor of Class A using concept of Method Resolution Order(MRO)    
        print("In C __init__")
    
    def feature(self):
        super().feature2()           # Calling Parent Class method using Super keyword
        super().feature3() 
        

obj = C()

obj.feature1() # It will also call feature-1 of Class A Using MRO
 
obj.feature()  

     
"""
MRO(Left to Right):-
Whenever we have multiple Inheritance It will always Starts from left to right mreans
first calls _init_ of left Class the call _init_ of right Class

Same can done with methods. 
"""
        
        
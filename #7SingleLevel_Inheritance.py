class A:               # Parent Class / Super Class
    def feature1(self):
        print("Feature 1 Working")
        
    def feature2(self):
        print("Feature 2 Working")

class B(A):               # Child Class / Sub Class of Parent Class "A" Now we can also use/access A Class function in B Class
    def feature3(self):
        print("Feature 3 Working")  
        
obj1 = A()
obj1.feature1()
obj1.feature2()

obj2 = B()
print("'B' class function after Inherating from A Class")
obj2.feature1()
obj2.feature2()
obj2.feature3()

"""
Sub Class can access all features of Super Class
                   But
Super Class can not access any feature of Sub Class
"""


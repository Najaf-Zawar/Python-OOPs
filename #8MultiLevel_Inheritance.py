class A:       # Parent Class / Super Class
    def feature1(self):
        print("Feature 1 Working")
        
    def feature2(self):
        print("Feature 2 Working")

class B(A):    # Child Class / Sub Class of Parent Class "A". Contain all the features of class "A"
    def feature3(self):
        print("Feature 3 Working") 
        
class C(B):    # GrandChild Class. Contain all features of Class "A" & "B" 
    def feature4(self):   
        print("Feature 4 Working") 
        
obj1 = A()
obj1.feature1()
obj1.feature2()

obj2 = B()
print("-->'B' class function after Inherating from 'A' Class")
obj2.feature1()
obj2.feature2()
obj2.feature3()


obj3 = C()
print("-->'C' class function after Inherating from 'B' Class")

obj3.feature1()
obj3.feature2()
obj3.feature3()
obj3.feature4()
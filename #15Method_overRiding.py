"""     
Method overRiding:-
Two methods with same name and same parameters/arguments not in same
class. Let we have two classes having inheritance Class A & class B(A)
and both the classes have same method with same parameters this is called 
Method overRiding.
"""

class A:
    def show(self):
        print("In A showm")
        

class B(A):
    def show(self):       # Class A method Override
        print("In A show")

obj = B()
obj.show()
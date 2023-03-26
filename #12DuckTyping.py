"""
Famous Line:
If there is a bird which is waking like a duck, quaking like a duck & which is swimming like a duck then that bird is a Duck.

which simply means it doesn't matter whether it is a duck or not what matters is behaviour of the bird if it is matching with a duck then it is a duck.
"""
# Python has concept of Dynamic Typing which means thhe type we can mention later. i.e

x = 5 # Here type we are representing now is Integer

x = "Najaf" # Are we changing the type of x here ?

"""
Ans:- That's not the case when we say 5 we got a space in our memory which is of type Integer & when
we say "Najaf" we got a space which is of type String 'x' is just a name of it we don't have specific 
type to x when we say 'type(x)' we are actually getting the type of 5 / "Najaf".
"""

class PyCharm:
    def execute(self):
        print("Conpiling")
        print("Running")
        
class MyIde:
    def execute(self):
        print("spell Check")
        print("convention Check")
        print("Conpiling")
        print("Running")
       
class Laptop:
    def code(self, ide):  
        ide.execute()
        # Is ide type fixed to PyCharm b/c I want to change Ide?
        """
        Ans:- Not exactly b/c this is dynamic typing so we can change the id 
        from PyCharm to MyIde provided we have the method execute. It doesnot
        which class object we are passing what matter is that class object has execute() method.
        
        From above famous line In same way if there is an object which is ide & if there has a method 
        execute() that its we are not concerned about what class object it is we are concerned about it
        should have method which is execute() that is called as Duck Typing. 
        In java we have concept of Interfaces and that what we do we cretae Interfaces and we have this PyCharm
        and MyIde as a class which will be implement as an Interface.
        """
        
        
ide = PyCharm()  

lap = Laptop()

lap.code(ide)
    
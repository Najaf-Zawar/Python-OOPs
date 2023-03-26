"""
Python doesnot support Abstraction ByDefault so we use it
by Importing module ABC stands for Abstract Base Classes to create 
our own Abstract classes.

Abstract Method:-
  Method which only have defination not a declaration we called them
  as Abstract Method.
Abstract Class:-
  The Class which will have Absttract Method is called Abstract Class.
  * we cann't create/instantiate object of Abstract Classes.
  * will have at least one Absttract Method
""" 
from abc import ABC , abstractmethod
class Computer(ABC):     
    @abstractmethod
    def process(self):     # Abstract Method
        pass
# Computer is a fancy term we actually buy laptops, desktops etc   
class Laptop(Computer):   # We have to Implement all methods of Abstract Class
    
    def process(self):     # Compultion for us to define the above Abstract Class method otherwise  it gives !Error
        print("Its Running")
       

#com = Computer()  # Give !Error b/c cann't Instantiate object of Abstrat Class
lap = Laptop()
lap.process()
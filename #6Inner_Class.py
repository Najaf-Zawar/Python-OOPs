### Used when we know this class can be used for specific Class then we don't need to Create another file for Class ###
class Student:       # Outer Class
    def __init__(self,name,rollNo): 
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()  # Creating object of Inner Class In Constructor(called automatically while Creating Object)
           
    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()
        
    class Laptop:    # Inner Class
        def __init__(self):  
           self.brand = "HP"
           self.cpu = "i5"
           self.ram = 8
           
        def show(self):
            print(self.brand, self.cpu, self.ram)
            

s1 = Student("Najaf", 220)
s2 = Student("Ali", 230)

s1.show()

lap1 = s1.lap   # When Create Object in Inner Class

lap1.show()

lap2 = Student.Laptop() # Directly Creating the object of Inner Class Outside Outer Class

lap2.show()

"""
Object Creation of Inner Class:
1. We can Create object of Inner Class inside the outer Class
                           OR         
2. We can Create object of Inner Class otside the Outer Class
   provided we Use Outer class name to call it.      

"""
class Computer():                     # Class is a blueprint or say Design 
    def config(self):                 # Self recieves object of class as argument
        print("i5, 6th, 16GB, 1TB")
      

# Creating object/instance of Class Computer
com1 = Computer()    
com2 = Computer()

# Calling the Computer function using class &  here we have to pass object as an argument explicitly as Self
Computer.config(com1) 
Computer.config(com2)

# Calling using object & here we don't need to pass object as an argument explicitly rather then it passes implicitly(Automatically)
com1.config()  
com2.config()


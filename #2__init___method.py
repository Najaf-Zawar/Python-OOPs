class Computer():
    def __init__(self, cpu, ram):  # __init__ mehod is just like constructor it will be getting called automatically while object Creation
        # Passing our arguments cpu & ram to object
        self.cpu = cpu             
        self.ram = ram
    
    def config(self):
        print(f"Config is {self.cpu}, {self.ram}")
        
com1 = Computer("i5",16) # object creation
com2 = Computer("Ryzen 3", 8) 

"""
Note:
Every time we create object it can allocate some memory /space in heap memory with some address & Constructor(i.e Computer()) allocates
size(depends on no. of vaiables) to Object in memory.

"""

com1.config()
com2.config()


        
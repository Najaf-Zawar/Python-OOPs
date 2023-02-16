class Person:
    def __init__(self):
        self.name = "Najaf"
        self.age = 23
        
    def update(self, age):
        self.age = age
    
    def compare(self, other):
        if self.age == other.age:
            print("They have same age")
        else:
            print("They have different age") 
            

p1 = Person()
p2 = Person()

print(id(p1)) # Print address of P1 object
print(id(p2)) # Print address of P2 object

print(p1.name)  # Before changing

p1.name = "Mahdi"    

print(p1.name)  # After changing

print(p2.age)

p2.age = 25    # changing directly

print(p2.age)

p1.update(28) # changing through update function & here p1 is passing as self

print(p1.age)  # After changing through upadte Function

p2.compare(p1)   # Here P2 is passing as self argument


   
    
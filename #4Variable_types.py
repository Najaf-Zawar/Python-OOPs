class car:
    wheels = 4                        # Class Variable defined in class namespace outside __init__(Same for all instances/objects)
    def __init__(self, model, mil):
        self.model = model            # Instanace variable defined in Instance namespace inside __init__(Every Insatnce have its own value)   
        self.mil = mil      


honda  = car("EK", 15)
kia = car("Picanto", 20)

honda.mil = 13  # Modify Instance variable value using Instance name

print(car.wheels)
car.wheels = 8 # Modify Class variable value using Class name b/c its Class variable

print(honda.model, honda.mil, honda.wheels)
print(kia.model, kia.mil, kia.wheels)


""" 
Namespace in an area where we create & store object/variable 
"""      
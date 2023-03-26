# Using Iterator we can print/fetch one value at a time.

lst = [1, 2 , 3, 4]

it = iter(lst)  # creating iterator object

print(it.__next__()) # Iterator can print 1 value at a time
 
# Iterator can store/preserve old value so everytime we call .next we get the next value 

print(next(it))  # Another way of printing
 

for i in lst:
    print(i)

# Creating our own Iterator
class TopTen:       # Gives us first 10 numbers
    def __init__(self):
        self.num = 1
        
    def __iter__(self): # Gives us object of Iterator
        return self
    
    def __next__(self): # Gives us next value/object
        if self.num <= 10:
            val = self.num
            self.num += 1
            
            return val
        else:
            raise StopIteration  # For loop handle exception Internally
        


values = TopTen()

print(next(values))  # It will gives us 1 so not repeat the value 1 again in loop

for i in values:
    print(i)

 
 
        
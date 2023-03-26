"""
Generators gives us Iterator
Function can be conveted to genrator using yield keyword instead of return.
So, Generator can return value in form of Iterator.  
* Return will terminate the function but yield will not
"""

def gen():
    yield 1
    yield 2
    yield 3
    
val = gen()

print(val.__next__())
print(val.__next__())

for i in val:  # print all remaning values
    print(i)  
    
    
# Generator to Print Square of Top 10 values
print("Top 10 Squares:")
def TopTen():
    n = 1
    
    while n <= 10:
        sq = n*n
        yield sq
        n += 1 
        
values = TopTen()

for i in values:
    print(i)
        

    
    
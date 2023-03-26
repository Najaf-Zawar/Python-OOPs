"""
Method overLoading:- (Python doesn't have support this Concept)
Two methods with a same name with different parameters/arguments it is
called Method overLoading i.e:- 
class Student:
      
      def avg(a, b)
      
      def avg(a, b, c)
"""

class Student:  
                
      def sum(self, a=None, b=None, c=None):  # Method OverLoading using trick b/c python doesn't support directly(Not work when arguments > 3)
            s = 0
            if a!=None and b!=None and c!=None:
                  s = a + b + c
            elif a!=None and b!=None:
                  s = a + b     
            
            return s
      
      # Other approach using variable Length argument (Generic even arguments > 3)      
      def add(self,a, *b):   # Minimum two arguments 'b' will receive value in form of tuple
            s = a
            for i in b:
                  s += i
            return s
            
             
             
            
s = Student()

print(s.sum(1,2,3))
print(s.sum(1,2))
print(s.sum(1))

print(s.add(1,2,3)) # 1 will assigned to 'a' & other two values'2, 3' assigned to 'b' in form of tuple 

            
        
    

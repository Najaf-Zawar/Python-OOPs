"""
Types of Errors:
1)Compile time Error: Easy to handle b/c error on developer side
     Syntax/Syntatical Error i.e Missing ':' OR Wrong Spelling.
     
2)Logical Error(Wrong Ouotput): Solve during testing(i.ebugs)
    In Logical error code gets compiled and give us output but(Wrong Output).
    
3)Runtime Error:  Most Difficult b/c mistake is done by User
    Code get compiled no syntax Error, no Logical Error but get error b/c of user 
    input at runtime(while code is running) i.e Divided by zero
    * When runtime error occurs execution will get stops.
"""
                    ########
"""
Two types of Statements in Code:
 1-Normal(will not give any Error) 
 2- Critical(We don't Know whether / not gives Error so we write them in try block)
"""

"""
For different types of errors we have different name as well i.e Divided by zero error
has name 'ZeroDivisionError' & wrong input error has name 'ValueError' & general one 
is Exception(It handle Everything).
"""

a = 5    # Normal Statement
b= 2

try:
    # When we open the resource it is compulsory to close it so tht's why we close it in finally block.
    print("Resource Open")
    print(a/b) # Critical Statement
    val = int(input("Enter a Number:")) #  Recieve integer value otherwise gives us Error
    print(val) 
          
except ZeroDivisionError as e:  # Handle when exception occurs while dividing by zero.
    print("Cann't divide a Number by Zero",e)
    
except ValueError as e: # Handle when exception occurs when gives wrong input in val i.e input = n.
    print("!Invalid Input") 
     
except Exception as e: # Handle the error which we don't know
    print("Something went Wrong...")
    
finally:     # Finally block will execute either exception occurs / not.
    print("Resource Closed")

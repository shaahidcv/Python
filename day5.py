# NOTE: module :

# import module_name

import math
from random import choice


print(math.pi)
print(math.sqrt(16))

print(choice(["x", "y", "z"]))  # random module choice function.


#NOTE: pip uses to install 3rd party libraries to our file.  eg: django



# pip install module_name

#NOTE: exceptions are the error messages when try to miss cast or divied by zero etc. 


#NOTE: build in exception 

    # syntaxError
    # TypeError
    # OSError
    # ImportError
    # ZeroDivisionError
    # NameError
    # IndexError
    # KeyError
    # ValueError
    # AttributeError
    # KeyboardInterrupt


#NOTE: exception handling:

integer = input("enter a integer:")

try:
    print(int(integer))
except ValueError:
    print("Error: Invalid input. Please enter a integer.")
else:
    print("No exception occurred.")
finally:
    print("This block will always run.")

#NOTE: if the try block worked then else case also work. if except works then else wont work.

#NOTE: finally block always run.
#NOTE: we can handle multiple except statements.

#NOTE: Why? OOP involves abstract concepts like "objects," "classes," "inheritance," and "polymorphism." These are not immediately tangible, making them harder to grasp.



# Solution: Relate these concepts to real-world examples. For instance:
#NOTE: A class is like a blueprint (e.g., a blueprint for a car).
#NOTE: An object is an instance of the class (e.g., a specific car built from the blueprint).
#NOTE: Methods are actions (e.g., driving the car).
#NOTE: Attributes are properties (e.g., the car’s color). 


# Solution: Build small projects using OOP:2
# Create a Car class with attributes like color and methods like drive.
# Build a BankAccount class to model real-world banking.
5
# fibonacci 

num = int(input("enter a number"))

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    a,b=0,1
    for _ in range(1 , num+1):
        a,b = b, a+b
        print(b)
    return b


fib(num)
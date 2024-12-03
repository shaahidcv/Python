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
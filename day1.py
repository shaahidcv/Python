full_name = "world" 
print(f"hello {full_name}")
age =25  #integer value
print(f"you are {age} years old")
gpa = 3.5 #float value
print(f"your gpa is {gpa}") 
is_staff = False #boolean value
# print(f"are you a staff : {is_staff}")  
#f string used to insert a variable. use {} to take variable name  


if is_staff:
    print("you are a staff")
else:
    print("you are not a staff")

# boolean values are often used with a if statement
# if statement is used to execute a block of code if a condition is met

# arithmetic expressions
num1 = 1 #integer
num1 += 8 #integer
print(num1)

# python dont have increment/decrement
# we can use + , - , * , / division returns a float , // integer divison, % .

#typecasting :  is a process of converting a variable from one data type to another.

name = "john"
age2 = 26
gpa2 = 4.5
is_student = True

# type is used to get the data type of variable

print(type(gpa2)) 

#output : <class 'float' >

gpa2 = int(gpa2)

print(type(gpa2))

#taking an input from user

# name3 = input("enter your name : ")
# print(name3)



# if statement 

# age4 = int(input("enter your age : "))
# if age4 >= 18:
#     print("you can vote")
# else:
#     print("you cant vote")


#elif statement

# age = int(input("enter your age : "))
# if age >= 18:
#     print("you can vote")
# elif age <= 0:
#     print("invalid input")
# else:
#      print("you cant vote")
    
    
# logical operators = evaluate multiple conditions (and,or, not)
# or operator : atleast one condition must be true
# and operator :both condition must be true
# not operator : it is used to reverse the condition

temp = 25
is_raining = True


# in here if one of the condition is true we excute the if statement
if temp > 35 or temp < 0 or is_raining:
    print("the event is cancelled")
else:
    print("the event is going on")

# both condition must be true to excute the if statement when writing with and operator

if temp >=20 and is_raining:
    print("it is too hot and rainy")
else:
    print("it is not too hot and not rainy")

# not makes the conditional if the condition is true it makes the condition false.

#while loop
# is used to repeat a block of code as long as a condition remains 'true' we recheck the condition at the end of the loop

#if somebody entered somethimg that is not correct while loop to check

# name= input("enter your name")

# def new_func(name):
#     while name== "":
#         name = input("enter your name")

#     print(f"your name is {name}")

# new_func(name)



# INFO: for loop : is used to iterate over a sequence (str, list, tuple,set) repeat the block of code an exact amount of times.


for i in range(1, 11, 2): #NOTE:1st number is inclusive and 2nd number is exclusive and 3rd is increment or decrement.
    print(i)

name = "shaahid"

for letter in name:
    print(letter, end="-")

# NOTE: here end="" separate each letter with -.


# we can also use end="\n" to separate each letter with a new line.
# we can also use end=" " to separate each letter with a space.

for i in range (10,0,-1):
    print(i)






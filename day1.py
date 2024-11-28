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

age4 = int(input("enter your age : "))
if age4 >= 18:
    print("you can vote")
else:
    print("you cant vote")


#elif statement

# age = int(input("enter your age : "))
# if age >= 18:
#     print("you can vote")
# elif age <= 0:
#     print("invalid input")
# else:
#      print("you cant vote")
    
    
# faherheit to celsius

fahrenheit = 52
celsius = (fahrenheit - 32) / 1.8
print(f"celsius = {celsius}")


# BMI 


print("BMI calculator")
height = 174
mass = 56

bmi = mass / height ** 2
print(f"BMI = {bmi}")


#  a Pythagorean theorem

a = int(input("enter the  length of a short side: "))
b = int(input("enter the length of another short side: "))

c = (a**2+b**2)**0.5
print(f" the length of the hypotenuse is  {c}")


#  Quadratic formula

a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))

if a == 0:
    print("a cant be zero")
else:
    x1 = (-b + (b**2 - 4 *a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4 *a*c)**0.5) / (2*a)





print(x1)
print(x2)
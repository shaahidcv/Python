 
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

#    curenncy exchanger

co = float(input("What do you have left in pesos?"))
pe = float(input("What do you have left in soles?"))
br = float(input("What do you have left in reais?"))

pesos_rate = 0.00023
soles_rate = 0.27
reais_rate = 0.16 

total_USD = (co*pesos_rate)+(pe*soles_rate)+(br*reais_rate)
print(f"Total amount in USD = {total_USD}")



import math

print("=======================")
print("Area Calculator  📐")
print("=======================")

print("1) Triangle \n2) Rectangle \n3) Square \n4) Circle \n5) Quit")
shape = int(input("Which shape: "))


if shape == 1:
    height = float(input("height: "))
    base = float(input("base: "))

    area = (height * base)/2
    print(f"area = {area}")
elif shape == 2:
    length = float(input("length: "))
    width = float(input("width: "))

    area = length * width
    print(f"area = {area}")
elif shape == 3:
    side = float(input("side: "))

    area = side **2
    print(f"area = {area}")

elif shape == 4:
    radius = float(input("radius: "))

    area = math.pi * (radius**2)
    print(f"area = {area}")

elif shape == 5:
    print("Thank you .....")
else:
    print("Enter a vaild input")



#NOTE: multiplication table:
import time

# num = 10# int(input("enter a number: "))
# if num ==0:
#     print("error")
# else:
#     for i in range(1,11):
#         print(f"{i} x {num} = {i*num}")
        


# for i in range(10,0,-1):
#     print(i,end=",")
#     time.sleep(.5)
# print("gooo.....")


# veg = ['carrot','chilli','tomato','onion']

# print(veg)
# print(veg[3])
# veg.append('garlic')
# veg.remove('carrot')
# for v in veg:
#     print(v,end=",")
# veg.clear()
# print(end="\n")
# print(veg)


# numbers = [65,15,32,78,10,6,1,98,54]

# print(numbers)
# number = numbers.copy()
# number.sort()
# print(number)
# even = [n for n in number if n%2==0]  #list comprension
# print(even)

numbers = []
size = int(input("enter the size"))

for i in range(size):
    num = int(input(""))
    numbers.append(num)

print(numbers)
sorted_array = numbers.copy()
sorted_array.sort()
print(sorted_array)


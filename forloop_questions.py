 #NOTE: question 1:

# for i in range(1,11):
#     print(i)


#NOTE: question 2:

# sum = 0
# for i in range(1,101):
#     sum = sum+i

# print(sum)


#NOTE: question 3:

# def fact(n):
#     if n<=0:
#         print("invalid number")
#     else:
#         f = 1
#         for i in range(1,n+1):
#             f = f*i
        
#         return f

# n = int(input("enter a number"))

# result = fact(n)
# print(result)

#NOTE: question 4:

# def fib(n):
#     a = 0
#     b = 1

#     if n <= 0:
#         print("invalid number")
#     elif n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)

#         for i in range(2,n+1):
#             c = a+b
#             a = b
#             b = c
#             if c <= n:
#                 print(c)
#             else:
#                 break

# n = int(input("enter a number"))
# fib(n)


#NOTE: question 5:

# my_dict = {'name':'shaahid','age':21,'marks':[20,50,80]}

# for key,value in my_dict.items():
#     print(f"{key} : {value}")

#NOTE: question 6:

# print("prime numbers between 1 and 50")

# for num in range(2,51):
#     is_prime = True
#     for i in range(2,int(num**0.5)+1):
#         if num%i ==0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=",")

#NOTE: question 7:

# for i in range(1,5+1):
#     print("*"*i)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#NOTE: QUESTION 8:

# for i in range(1,6):
#     for j in range(1,11):
#         print(f"{j} * {i} = {j*i}")
#     print()

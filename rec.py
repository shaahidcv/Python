def recursion(n):
    if n <= 0:
        return n
    else:
        return n + recursion(n-1)
    
print(recursion(13))

#NOTE: recursion: a function call its self.

#NOTE: lambda function: 

l = lambda x: x*x
print(l(10))



#NOTE: we can give multiple arguments but only one expression.


#problem 9 : prime number

# n = int(input("enter a number to check"))






# for loop

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, name in enumerate(names):
    print(f"{i}. {name}")




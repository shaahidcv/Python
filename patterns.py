# left side half pyramid star
num=5
for i in range(1,num+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print()




# right side half pyramid star 

for i in range(1,num+1):
    for j in range(0,num-i,1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print()


#right side inverted star pyramid

for i in range(1,num+1):
    for j in range(0,i-1):
        print(" ",end="")
    for j in range(0,num-i+1):
        print("*",end="")
    print()

# left side inverted star pyramid

for i in range(num,0,-1):
    for j in range(i):
        print("*",end="")
    print()


    num = 5  # Number of rows

# left side half pyramid hollow

for i in range(1,num+1):
    for j in range(1,i+1):
        if j==i or j==1 or num == i:
            print("*",end="")
        else:
            print(" ",end="")
    print()


#right side inverted half pyramid hollow

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(" ",end="")
    for j in range(i):
        if j==0 or j==i-1 or num == i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    



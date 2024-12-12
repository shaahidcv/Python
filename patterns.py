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



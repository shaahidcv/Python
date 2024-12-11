#multiplication

num = int(input("enter a number: "))

if num ==0:
    print("number must be more than zero.")
else:
    for i in range(1,num):
        print(f"{i} x {num} = {i*num}")


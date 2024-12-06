#NOTE: multiplication table:

num = int(input("enter a number: "))
if num ==0:
    print("error")
else:
    for i in range(1,11):
        print(f"{i} x {num} = {i*num}")



# print("hello world")


#NOTE: basic arithmetic 

# a=int(input("enter a number \n"))
# b=int(input("enter a number \n"))

# char = input("Enter a character")

# if char == '+':
#     print(a+b)
# elif char == '-':
#     print(a-b)

# elif char == '*':
#     print(a*b)

# elif char == '/':
#     if b != 0:
#         print(a/b)
#     else:
#         print("Error: Division by zero")


#NOTE: program to check odd or even.

# num = int(input("Enter a number"))

# if num%2==0:
#     print("Even number")
# else:
#     print("Odd number")

#NOTE: program to find factorial of a number.

# factorial = 1
# if num < 0:
#     print("Factorial is not defined for numbers less than 1")
# elif num==0:
#     print("Factorial is 1")
# else:
#     for i  in range(1,num + 1):
#         factorial = factorial*i

#     print("factorial of the",num,"is",factorial)


# simple banking program

def balance():
    print(f"Your current balance is ${banking_info[name]}")
    print("******************************")

def deposit():
    amount = float(input("Enter the amount to deposit:"))
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        banking_info[name] += amount
        print(f"Deposited successfully\nCurrent balance is ${banking_info[name]}")
        print("******************************")


def withdraw():
    amount = float(input("Enter the amount to be withdrawn:"))
    if amount < 0:
        print("Invalid amount")
        print("******************************")
        return 0
    elif amount > banking_info[name]:
        print("Insufficient balance")
        print("******************************")
        return 0
    else:
        banking_info[name] -= amount
        print(f"Withdrawn successfully\nCurrent balance is ${banking_info[name]}")
        print("******************************")



is_running = True
banking_info = {"alice":0,"bob":100,"fred":1500,"john":2000,}
print("******************************")

print("Welcome to the banking program")
name = input("Enter your name: ")

if name in banking_info:
    print(f"Access granted welcome {name}")
    while is_running:
        print("******************************")

        print("Banking program \n1. Show balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = int(input("Enter your choice (1-4):"))
        if choice == 1:
            balance()
        elif choice == 2:
            deposit()
        elif choice ==3:
            withdraw()
        elif choice == 4:
            is_running = False
        else:
            print("Enter a valid choice")
    print("Thank you for using our banking program")

else:
    print("Access denied")

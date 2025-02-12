 #NOTE: PASSWORD GENERATOR:

import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the password generator \n")
n_alpha = int(input("how many alphabets u want \n"))
n_number = int(input("how many numbers u want \n"))
n_symbol = int(input("how many symbol u want \n"))

password_list = []
for i in range(1,n_alpha+1):
    char = random.choice(alphabets)
    password_list += char

for i in range(1,n_number+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,n_symbol+1):
    char = random.choice(symbols)
    password_list += char

random.shuffle(password_list)
password= ""
for i in password_list:
    password += i
print(f"password is {password}")





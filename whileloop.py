#NOTE: question 9:

# num = 10
# while num >= 1:
#     print(num ,end=" ")
#     num -= 1
    

#NOTE: question 10:

# num = int(input("enter a number"))

# original = num
# reversed = 0

# while num > 0:
#     digit = num % 10
#     reversed = (reversed * 10)+ digit
#     num = num // 10

# if original == reversed:
#     print("number is palindrome")
# else:
#     print("not palindrome")

#NOTE: question 11:

# while True:
#     num = (input("enter 'exit' to quit : "))
#     if num == 'exit':
#         print("exiting the loop")
#         break
#     print(f"you entered {num}")

#NOTE: question 12:

# num = 99
# sum = 0

# while num !=0:
#     digit = num % 10
#     sum += digit
#     num = num // 10

# print(sum)
    
#NOTE: question 13:

# while True:
#     num = int(input("guess the number"))
#     if num == 6:
#         print("u guessed right")
#         break
#     print("your guess is wrong")

#NOTE: question 14:

# my_list = [10,20,30,45,50]

# count = 0

# for i in my_list:
#     count += 1

# print(count)

#NOTE: question 15:

# my_list = [10,20,30,45,50]

# sum = 0

# for i in my_list:
#     sum = sum + i

# print(sum)

#NOTE: question 16:

# my_list = [10,20,30,45,50]

# largest = my_list[0]

# for i in my_list:
#     if i > largest:
#         largest = i
#     else:
#         pass

# print(largest)

#NOTE: question 17:

# my_list = [10,20,30,45,50,1]

# mini = my_list[0]

# for i in my_list:
#     if i < mini:
#         mini = i
#     else:
#         pass

# print(mini)

#NOTE: question 18:

# my_list = [10,20,30,45,50,1]

# reversed = []

# for i in range(len(my_list)-1,-1,-1):
#     reversed.append(my_list[i])

# print(reversed)

#NOTE: question 19:

# my_list = [10,20,6,86,15,30,45,50,1]

# largest = 0
# second_largest = 0

# for i in my_list:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i


# print(second_largest)

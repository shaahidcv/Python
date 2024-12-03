numbers = [10,20,56,60,18,57,23,4]

# sum = sum(numbers)
# print("Sum of the list is: ", sum)  
# max = max(numbers)
# print("Maximum value in the list is: ", max)

# min = min(numbers) 
# print("Minimum value in the list is: ", min)


# NOTE: without function

sum = 0
for i in numbers:
    sum = sum+i

print("Sum of the list is: ", sum)

min = numbers[0] # initialize to first element of list
max = numbers[0] # initialize to first element of list

for i in numbers:
    if i < min:
        min = i
    if i> max:
        max = i

print("Minimum value in the list is: ", min)
print("Maximum value in the list is: ", max)


#palindrome

word = input("enter a word to check palindrome or not:")

normal_word = word.lower()
reversed_word = ""
for i in range(len(normal_word)-1,-1,-1): 
    reversed_word += normal_word[i]

if normal_word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome." )

#simple interest:

principal = 5000
rate_of_interest = 5
time = 2

simple_interest = (principal*rate_of_interest*time)/100
print(simple_interest)
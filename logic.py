#NOTE: Patterns for logic building :
#pattern problems:

#   1) square star pattern
for i in range(4): # outer loop determines the number of rows.

    for j in range(4): # inner loop for column
        print("#",end="")

    print()

# Outer Loop (for i in range(rows)):

# Runs 3 times (once for each row).
# Each iteration represents a single row.


# Inner Loop (for j in range(columns)):

# Runs 5 times for each row.
# Prints 5 stars in one row.

# print('*', end=''):
# Prints a star without moving to a new line.

# print() after the inner loop:
# Moves to the next row.

#NOTE: Outer loop: "How many rows do I want?" AND Inner loop: "How many stars in each row?".


# 2) inverted pyramid star pattern:
num=5
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()








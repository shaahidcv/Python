def fib(n):
    a = 0
    b = 1

    if n <= 0:
        print("invalid number")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n+1):
            c = a+b
            a = b
            b = c
            if c <= n:
                print(c)
            else:
                break

n = int(input("enter a number"))
fib(n)



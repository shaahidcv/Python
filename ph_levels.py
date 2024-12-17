ph = int(input("enter ph value (0 to 14):"))

if ph > 7:
    print("basic")
elif ph < 7:
    print("acid")
else:
    print("neutral")
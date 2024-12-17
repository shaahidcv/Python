height = int(input("enter your height in (cm) : "))
credits = int(input("enter your credits: "))

if height >= 133 and credits >= 10:
    print("Enjoy the ride!")
elif height >= 133 and credits <= 10:
    print("You don't have enough credits.")
elif height <= 133 and credits >= 10:
    print("You are not tall enough to ride.")
else:
    print("not met either requirement.")
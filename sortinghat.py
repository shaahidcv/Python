q1 = int(input("Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n"))
q2 = int(input("When I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n"))
q3 = int(input(" Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n"))

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


if q1 == 1:
    Gryffindor = 1
    Ravenclaw = 1
elif q1 == 2:
    Hufflepuff = 1
    Slytherin = 1
else:
    print("error...! invalid input")



if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Gryffindor += 2
elif q2 == 4:
    Ravenclaw += 2
else:
    print("error....! invalid input")


if q3 == 1:
    Slytherin += 4
    
elif q3 == 2:
    Hufflepuff += 4
    
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Slytherin += 4
    
else:
    print("error....! invalid input")

print(f"🦁 Gryffindor: {Gryffindor}")
print(f"🦅 Ravenclaw: {Ravenclaw}")
print(f"🦡 Hufflepuff: {Hufflepuff}")
print(f"🐍 Slytherin: {Slytherin}")


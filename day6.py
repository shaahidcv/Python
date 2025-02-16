    #NOTE: define a class
from Car import Car
from Car import Student

car_1 = Car("chevy","corvette",2021,"blue")

# call methods
print(car_1.make)
car_1.drive()


student1 = Student("alice","A")
Student2 = Student("bob", "A")

student1.display()
Student2.display()

car_1.stop()

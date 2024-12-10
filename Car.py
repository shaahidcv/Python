class Car:
    

    def __init__(self, make, model, year, color):
        self.make = None
        self.model =  model
        self.year = None
        self.color = None

    def drive(self):
        print("this "+self.model+" is driving.")

    def stop(self):
        print("this car is stopped.")



#NOTE: problem 2

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"student name is {self.name} and grade is {self.grade}")

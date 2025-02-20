class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

dog = Dog("scooby")
cat = Cat("garfield")
bird = Bird("dodo")

print(dog.name)
print(dog.is_alive)

cat.sleep()



#NOTE: problem 2 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

    def display_salary(self):
        print(f"{self.name} earns ${self.salary}")


class Manager(Employee):

    def work(self):
        print(f"{self.name} is managing")


person1 = Manager("rizal", 100000)
person2 = Employee("sinan", 50000)

person1.work()
person2.work()

person1.display_salary()
person2.display_salary()

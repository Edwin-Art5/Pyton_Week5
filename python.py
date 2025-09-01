# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand # attribute
#         self.model = model

#     def drive(self): # method
#         print(f"{self.brand} {self.model} is driving!")


# # create object
# my_car = Car("Toyota", "Caldina")
# my_car.drive()

# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

# student1 = Person(21, "John Doe")
# print(student1.name)
# print(student1.age)

class Car:
    def move (self):
        print("Driving")

class PLane:
    def move (self):
        print("Flying")

class Boat:
    def move (self):
        print("Sailing")

class Dog:
    def move (self):
        print("Running")

Car = Car()
PLane = PLane()
Boat = Boat()
Dog = Dog()

vehicles_and_animals = [Car, PLane, Boat, Dog]

for item in vehicles_and_animals:
    item.move()
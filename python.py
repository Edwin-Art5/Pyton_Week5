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
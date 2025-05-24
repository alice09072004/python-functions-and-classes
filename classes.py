# classes.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

    def say_goodbye(self):
        return f"{self.name} says goodbye!"

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound!"

    def describe(self):
        return f"{self.name} is a {self.species}."

class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def start_engine(self):
        return f"The {self.model} engine starts."

    def describe(self):
        return f"This is a {self.color} {self.model}."



# Get user input for Person
person_name = input("Enter the person's name: ")
person_age = int(input("Enter the person's age: "))
person1 = Person(person_name, person_age)
print(person1.greet())
print(person1.say_goodbye())

# Get user input for Animal
animal_species = input("Enter the animal species: ")
animal_name = input("Enter the animal's name: ")
animal = Animal(animal_species, animal_name)
print(animal.make_sound())
print(animal.describe())

# Get user input for Vehicle
vehicle_model = input("Enter the vehicle model: ")
vehicle_color = input("Enter the vehicle color: ")
vehicle = Vehicle(vehicle_model, vehicle_color)
print(vehicle.start_engine())
print(vehicle.describe())



# Import functions and classes from the other files
from functions import greet, add_numbers, multiply_numbers, is_even
from classes import Person, Animal, Vehicle

# Call the functions from function.py
print(greet("Alice"))  # Example usage of greet function
num1 = int(input("Enter a number to add: "))
num2 = int(input("Enter another number to add: "))
print(f"The sum is: {add_numbers(num1, num2)}")

num1 = int(input("Enter a number to multiply: "))
num2 = int(input("Enter another number to multiply: "))
print(f"The product is: {multiply_numbers(num1, num2)}")

num = int(input("Enter a number to check if it's even: "))
print(is_even(num))

# Call the classes from classes.py
# Person class
person_name = input("Enter the person's name: ")
person_age = int(input("Enter the person's age: "))
person1 = Person(person_name, person_age)
print(person1.greet())
print(person1.say_goodbye())

# Animal class
animal_species = input("Enter the animal species: ")
animal_name = input("Enter the animal's name: ")
animal = Animal(animal_species, animal_name)
print(animal.make_sound())
print(animal.describe())

# Vehicle class
vehicle_model = input("Enter the vehicle model: ")
vehicle_color = input("Enter the vehicle color: ")
vehicle = Vehicle(vehicle_model, vehicle_color)
print(vehicle.start_engine())
print(vehicle.describe())

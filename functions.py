def greet(name):
    return f"Hi {name}, welcome!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def is_even(num):
    if num % 2 == 0:
        return f"Computer Output: {num} is even "
    else:
        return f"Computer Output: {num} is odd "


name = input("Enter your name: ")
print(greet(name))

num1 = int(input("Enter the first number for addition: "))
num2 = int(input("Enter the second number for addition: "))
print(f"Sum: {add_numbers(num1, num2)}")

num1 = int(input("Enter the first number for multiplication: "))
num2 = int(input("Enter the second number for multiplication: "))
print(f"Product: {multiply_numbers(num1, num2)}")

num = int(input("Enter a number to check if it's even or odd: "))
print(is_even(num))



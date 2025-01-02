# Part 1: Using Built-in Functions and Aliases
from math import sqrt, pi  # Import specific functions

# Calculate the area of a circle
radius = 5
area = pi * radius**2
print(f"Area of the circle: {area}")  # Output: 78.53981633974483

# Using math functions with an alias
import math as m
result = m.sqrt(25)
print(f"Square root of 25: {result}")  # Output: 5.0


# Part 2: Creating and Using a Module
# Simulating the content of 'my_module.py'
def greet(name):
    print("Hello, " + name + "!")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Using the module
greet("Alice")  # Output: Hello, Alice!
result = factorial(5)
print(f"Factorial of 5: {result}")  # Output: 120


# Part 3: Creating and Using a Package
# Simulating the package structure
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Simulated content of 'my_package.module1'
def add(x, y):
    return x + y

# Simulated content of 'my_package.module2'
def subtract(x, y):
    return x - y

# Using the package
result1 = add(5, 3)
result2 = subtract(10, 4)

print(f"Result of addition: {result1}")  # Output: 8
print(f"Result of subtraction: {result2}")  # Output: 6

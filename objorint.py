# Part 1: Class Example
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"Starting the {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

# Calling methods
car1.start()  # Output: Starting the Toyota Camry
car2.start()  # Output: Starting the Honda Civic


# Part 2: Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Creating an object of the derived class
dog1 = Dog("Buddy")
dog1.eat()   # Output: Buddy is eating.
dog1.bark()  # Output: Buddy is barking.


# Part 3: Polymorphism Example
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 3)

print(f"Circle Area: {circle.area()}")     # Output: Circle Area: 78.5
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 12

# Polymorphic function example
def add(a, b=0, c=0):
    return a + b + c

print(add(2, 3))       # Output: 5
print(add(2, 3, 4))    # Output: 9


# Part 4: Encapsulation Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance")

# Using the class
account = BankAccount(1000)
account.deposit(500)   # Output: Deposited 500. New balance: 1500
account.withdraw(200)  # Output: Withdrew 200. New balance: 1300

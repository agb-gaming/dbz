# Exception Handling
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid input types")
    else:
        print("Division successful")
    finally:
        print("This block always executes")

print("Exception Handling Examples:")
divide(10, 2)  # Valid division
divide(10, 0)  # Division by zero
divide("a", "b")  # Invalid input types

print("\n")


# User-Defined Exception
class NegativeNumberError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeNumberError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("User-Defined Exception Example:")
try:
    result = factorial(-5)
except NegativeNumberError as e:
    print(e)  # Handling the custom exception

try:
    print("Factorial of 5:", factorial(5))
except NegativeNumberError as e:
    print(e)

print("\n")


# Multithreading
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")

def print_letters():
    for char in 'abcde':
        print(f"Letter: {char}")

print("Multithreading Example:")
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start both threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Both threads have completed execution")

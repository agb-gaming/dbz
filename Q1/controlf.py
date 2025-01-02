# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#switch


print("here switch cases start")


# Simple calculator using a dictionary to mimic switch
def calculator(a, b, operation):
    switch = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else "Division by zero error"
    }
    return switch.get(operation, "Invalid operation")

a = 10
b = 5
operation = "add"  # Try "subtract", "multiply", "divide", "invalid"
result = calculator(a, b, operation)
print(f"Result: {result}")

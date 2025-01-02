# Part 1: Working with JSON
import json

# JSON data as a string
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'

# Parsing JSON
data = json.loads(json_data)
print(f"Name: {data['name']}")  # Output: Alice
print(f"Age: {data['age']}")    # Output: 30
print(f"City: {data['city']}")  # Output: New York


# Part 2: Validations

# Password Validation
import re

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

password = input("Enter your password: ")
if validate_password(password):
    print("Valid password")  # Output depends on input
else:
    print("Invalid password")  # Output depends on input


# Email Validation
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, email) is not None

email = input("Enter your email: ")
if validate_email(email):
    print("Valid email")  # Output depends on input
else:
    print("Invalid email")  # Output depends on input


# URL Validation
def validate_url(url):
    regex = (
        r"^(https?://)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b"
        r"([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    )
    return re.fullmatch(regex, url) is not None

url = input("Enter a URL: ")
if validate_url(url):
    print("Valid URL")  # Output depends on input
else:
    print("Invalid URL")  # Output depends on input


#Password123!
#user@example.com
#https://www.example.com
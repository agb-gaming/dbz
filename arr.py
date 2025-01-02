# NumPy Array Creation and Operations
import numpy as np

# 1D Array Creation
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)

# 2D Array Creation
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# Array Operations (Addition, Subtraction, Multiplication, Division)
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])

print("\nArray Operations:")
print("Addition:", arr3 + arr4)
print("Subtraction:", arr3 - arr4)
print("Multiplication:", arr3 * arr4)
print("Division:", arr3 / arr4)

# Searching and Sorting in Arrays
arr5 = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

print("\nSearching and Sorting in Array:")
# Sorting
sorted_arr = np.sort(arr5)
print("Sorted Array:", sorted_arr)

# Finding Unique Elements
unique_elements = np.unique(arr5)
print("Unique Elements:", unique_elements)

# Finding Indices of Specific Values
indices = np.where(arr5 == 5)
print("Indices of 5:", indices)

# Date and Time Handling
import datetime

# Get Current Date and Time
now = datetime.datetime.now()
print("\nCurrent Date and Time:")
print(now)

# Specific Date and Time
specific_date = datetime.datetime(2023, 11, 25, 12, 30)
print("\nSpecific Date and Time:")
print(specific_date)

# Formatting Dates and Times
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
print("\nFormatted Date and Time:")
print(formatted_date)

# String Handling
text = "Hello, World!"

print("\nString Handling:")
# Length of the string
print("Length of the string:", len(text))

# Slicing the string
print("Sliced String (First 5 chars):", text[0:5])

# Concatenation
new_text = text + " How are you?"
print("Concatenated String:", new_text)

# Finding Substrings
index = text.find("World")
print("Index of 'World' in the string:", index)

# 1. Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

string = "racecar"
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")


# 2. Check if a number is a prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# 3. Check if two strings are anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")


# 4. Generate the Fibonacci series up to n terms
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[i-1] + fib_series[i-2])
        return fib_series

n = 10
print(f"Fibonacci series (first {n} terms): {fibonacci(n)}")


# 5. Check if a number is a perfect number
def is_perfect_number(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num

num = 28
if is_perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

# Functions to test
def add(a, b):
    return a + b

def is_palindrome(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def multiply(a, b):
    return a + b  # intentionally wrong - should be a * b

def multiply(a, b):
    return a * b  
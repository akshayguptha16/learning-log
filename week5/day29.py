# Problem 1 — FizzBuzz
# Write a function that takes a number n and prints:


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0 :
            print("Fizzbuzz")  
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(i) 

    fizzbuzz(15)

# Problem 2 — Count vowels
# Write a function that counts the number of vowels in a string.

def count_vowles(text):
    vowles = 'aeiouAEIOU'
    count = 0

    for char in text:
        if char in vowles:
            count += 1

    return count

# example
print(count_vowles("Hello World"))

# Problem 3 — Find duplicates
# Write a function that finds all duplicate numbers in a list and returns them.

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

# Example
nums = [1, 2, 3, 2, 4, 5, 1, 6, 3]
print(find_duplicates(nums))

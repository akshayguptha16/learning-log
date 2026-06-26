# Pythonic Python and Comprehensions

# List comprehension - numbers divisible by 3
numbers = [num for num in range(1, 21) if num % 3 == 0]
print(numbers)

# Dict comprehension - word lengths
words = ["python", "django", "api"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# Generator - squares of 1-10
squares = (num ** 2 for num in range(1, 11))
for square in squares:
    print(square)
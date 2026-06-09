#arrys 
def find_largest(number):
    if not number:
        return None

    largest = number[0]

    for num in number:
        if num > largest:
            largest = num

    return largest

# example 
num = [3, 7, 1, 9, 4, 6]
print(find_largest(num))

# Lists
def reverse_list(numbers):
    reversed_list=[]

    for i in range(len(numbers)-1, -1,-1):
        reversed_list.append(numbers[i])

    return reversed_list

numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers)) 

# Strings 
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1

    return True

# Examples
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("madam"))


def two_sum(numbers, target):
    seen = {} 

    for i,num in enumerate(numbers):
        complment = target - num 

        if complment in seen:
            return [seen[complment],i]

        seen[num] = i

    return []

numbers = [2, 7, 11, 15]
target = 9 

print(two_sum(numbers,target))
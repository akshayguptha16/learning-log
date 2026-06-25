# Problem 1 — Second Largest Number
# The idea is to track two variables simultaneously as you loop — largest and second.

# def second_largest(nums):
#     largest = float('-inf')
#     second = float('-inf')

#     for num in nums:
#         if num > largest:
#             second = largest
#             largest = num
#         elif largest > num > second:
#             second = num 

#     return second

# numbers = [10, 5, 20, 8, 15]
# print(second_largest(numbers)) 

# Problem 2 — Anagram Check
# Two strings are anagrams if they have exactly the same characters in the same quantities.
# def is_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False

#     count = {}

#     # count characters in first string 
#     for char in s1:
#         count[char] = count.get(char, 0)+1

#     # subtract counts using second string 
#     for char in s2:
#         count[char] = count.get(char, 0) - 1

#     #check all counts are zero 
#     return all(value == 0 for value in count.values())

# print(is_anagram('listen','silent'))
# print(is_anagram('hello ','world '))

# Problem 3 — Maximum Subarray (Kadane's Algorithm)
# This is the most famous greedy algorithm problem.

def max_subarray(nums):
    current_sum= nums[0] 
    max_sum = nums[0]

    for num in nums[1:]:
       if current_sum + num < num:
          current_sum = num
       else:
            current_sum += num
       if current_sum > max_sum:
            max_sum = current_sum
       
    return max_sum 

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
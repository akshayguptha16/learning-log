def length_of_longest(s):
    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


print(length_of_longest("abcabcbb"))   # 3
print(length_of_longest("bbbbb"))      # 1
print(length_of_longest("pwwkew"))     # 3
print(length_of_longest(""))           # 0


from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))


#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#


def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
print(product_except_self([1,2,3,4]))
print(product_except_self([2,3,4,5]))
print(product_except_self([-1,1,0,-3,3]))

# Day 3 - lists, loops, slicing, enumerate

# Cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# for city in Cities:
#     print(city)

# # Cities.append('Bengaluru')
# # print(Cities)
# # print(Cities[::-1])
# # print(Cities[0:3])

# # cities = ['New York', 'Los Angeles', 'Chicago']
# for index, city in enumerate(Cities):
#     print(f"{index + 1}. {city}")

# # num = [10, 20, 30, 40, 50]
# # total = 0
# # for n in num:
# #     total = total + n
# # print(f"The sum is {total} .")

# Day 3 - Lists and Loops

# Basic list and loop
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in cities:
    print(city)

# Slicing
print(cities[0:3])
print(cities[::-1])

# Append
cities.append('Bengaluru')
print(cities)

# Manual sum
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total = total + n
print(f"The sum is {total}.")

# Enumerate
for index, city in enumerate(cities):
    print(f"{index + 1}. {city}")
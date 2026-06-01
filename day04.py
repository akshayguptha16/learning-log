# 
# a = input("Enter your name: ")
# b = input("Enter your age: ")
# c = input("Enter your city: ")

# dict = {"name": a, "age": b, "city": c}
# print(dict)

# # print(f"My name is {a} and I am {b} years old and I live in {c}.")
# person = {"name": a, "age": b, "city": c}
# print(person)

# print(person["name"])
# print(person["age"])
# print(person["city"])

# for key in person:
#     print(f"{key}:{person[key]}")

# a = input("Enter your name: ")
# b = input("Enter your age: ")
# c = input("Enter your city: ")

# person = {"name": a,"city": c}

# for key, value in person.items():
#     print(f"{key}: {value}")

# # .items() is a method not a function, 
# # and it returns all key-value pairs as tuples 

# person["skills"] = {"python", "java", "c++"}
# print(person ["skills"])

# person["skills"] = ["Python", "Django", "SQL"]

# person["city"] = "Mumbai"

# del person["age"]

# for key, value in person.items():
#     print(f"{key}: {value}")

person = {
    "name": "Akshay",
    "age": "23",
    "skills": []
}

person["skills"] = ["Python", "Django", "SQL"]
person["city"] = "Mumbai"

del person["age"]

for key, value in person.items():
    print(f"{key}: {value}")
#==============================================================

# Day 4 is complete. Here's what you learned today:

# Creating dictionaries
# Accessing values by key
# Adding new keys
# Updating existing values
# Deleting keys with del
# Looping through dictionaries with .items()
# Difference between lists and sets
# Why data types matter 

#==============================================================#
# Day 4 - Dictionaries

# person = {"name": "Akshay", "age": 23, "city": "Bengaluru"}

# # Add a key
# person["skills"] = ["Python", "Django", "SQL"]

# # Update a value
# person["city"] = "Mumbai"

# # Delete a key
# del person["age"]

# # Print all key-value pairs
# for key, value in person.items():
#     print(f"{key}: {value}")

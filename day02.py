# def greet(name):
#     name = input("Enter your Name: ")
#     print(f"Hello, {name}! Welcome to the Python .")
# # greet()
# def greet(name):
#     print(f"Hello, {name}")
# print(greet("Akshay"))
# def greet(name):
#     return(f"hello, {name}!")
# print(greet("Akshay"))

# "This program defines a function called greet 
# that takes a name as a parameter and returns 
# a greeting string. 
# When we call greet("Akshay"), 
# it returns "Hello, Akshay!" and 
# we print that result."

#---------------------------------------------------------#
#---------------------------------------------------------#
#---------------------------------------------------------#

# a = int(input("Enter the year of Birth :"))
# age = 2026 - a
# print(f"You are {age} years old.")

# def calculate_age(year_of_birth):
#     current_year = 2026
#     # year_of_birth = int(input("Enter the year of Birth :"))
#     age = current_year - year_of_birth
#     return age

# year = int(input("Enter the year of Birth :"))
# print(f"You are {calculate_age(year)} years old.")


# Python calls calculate_age(year) first, gets the returned age number, plugs it into the f-string, 
# then prints the complete sentence. 
# The function runs inside the {} before the print happens.
# That's called function composition — using a function call directly inside another expression.
# You'll see this constantly in real code.

#-------------------------Day-02--------------------------------#

# # Function-1
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Akshay"))

# # Function-2
# def calculate_age(year_of_birth):
#     current_year = 2026
#     age = current_year - year_of_birth
#     return age

# year = int(input("Enter the year of Birth :"))
# print(f"You are {calculate_age(year)} years old.")

# Global variable - accessible everywhere
current_year = 2026
current_year = 2026

def calculate_age(year_of_birth):
    age = current_year - year_of_birth
    return age

year = int(input("Enter your birth year: "))
print(f"You are {calculate_age(year)} years old.")
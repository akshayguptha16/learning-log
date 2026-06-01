# Day 1
# f-strings, try/except, error handling


# # a = input("Enter your Name: ")
# # b = input("Enter your Age: ")
# # print("My name is " + a + " and i am " + b + " years old.")
# name = input("Enter Your Name:")
# age = input("Enter Your Age:")
# City = input("Enter Your City:")
# print(f"My name is {name} and I am {age} years old and I live in {City}.") 

# print("My name is {0}, and I am {1} years old and I live in {2}.".format(name, age, City))

# print("My name is ", name, "and I am ", age, " years old and I live in ", City, ".")

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return(a - b)

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Please enter a valid number"
#     return a / b

# while True:
#     print("Choose an operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "5":
#         print("Calculator Closed.")
#         break

#     if choice in ["1", "2", "3", "4"]:
#         a = num1 = float(input("Enter first number: "))
#         b = num2 = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result:", add(num1, num2))
#         elif choice == "2":
#             print("Result:", subtract(num1, num2))
#         elif choice == "3":
#             print("Result:", multiply(num1, num2))
#         elif choice == "4":
#             print("Result:", divide(num1, num2))
#     else:
#         print("Invalid choice. Please try again.")

try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number for the second input.")

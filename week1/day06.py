# # Inheritance.
# # the concept in one sentence — 
# # inheritance lets one class take 
# # all the attributes and methods of another class 
# # and add its own on top.
# # Real world example — every employee is a person.
# # So an Employee class should inherit everything 
# # from Person and just add job-specific details.
# # ================================================================ #
# # ---------------------------------------------------------------- #
# # ================================================================ #
# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #     def greet(self):
# #         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# # person = Person("Akshay",23)

# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     # Indented by 4 spaces to stay inside the class
# #     def greet(self):
# #         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# # # Outside the class
# # person = Person("Akshay", 23)
# # print(person.greet())




# # class Employee(Person):
# #     def __init__(self, name, age, company):
# #         super().__init__(name, age)  # Call the parent class's __init__ method
# #         # company = input("Enter your company name: ")
# #         self.company = company

# # company = Employee("Enter your company name: ")
# # print(company.introduce())

# # def introduce(self):
# #     return f"Hi i am {self.name}, I am {self.age} years old and I am working at {self.company}."

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# class Employee(Person):
#     def __init__(self, name, age, company):
#         super().__init__(name, age)  # Call the parent class's __init__ method
#         self.company = company

#     def introduce(self):
#         return f"Hi I am {self.name}, I am {self.age} years old and I am working at {self.company}."
    
# employee = Employee("Akshay", 23, "Sakshath Techonologies")
# print(employee.introduce())

# print(employee.greet())


# class student(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school

#     def introduce(self):
#         return f"Hi I am {self.name}, I am {self.age} years old and I study at {self.school}."
    
# student = student("Akshay", 23, "Jain University")
# print(student.introduce())
# print(student.greet())




# class Student():
#      def __init__(self, name, age, university):
#         self.name = name
#         self.age = age
#         self.university = university

# def Study(self):
#         return f"Hi I am {self.name}, I am {self.age} years old and I study at {self.school}."

# student = Study("Akshay", 23, "Jain University")
# print(student.Study())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def study(self):
        return f"Hi I am {self.name}, I am {self.age} years old and I study at {self.university}."
    
student = Student("Akshay", 23, "Jain University")
print(student.study())
print(student.greet())

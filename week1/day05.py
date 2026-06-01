# -----OOPS IN PYTHON----- #
#---CLASS---#
class Person:                                  # Class Person
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person = Person("Akshay",23)                     # Object "person" of class Person
person2 = Person("Rahul", 25)
person3 = Person("Priya", 22)
# print(person.name)
# print(person.age) 

# print(person.greet())
# print(person2.greet())
# print(person3.greet())

people = [person, person2, person3]
for p in people:
    print(p.greet())

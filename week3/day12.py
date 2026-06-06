import json
# Python dict to JSON string
person = {
    "name":"Akshay",
    "age": 20,
    "city": "Bangalore",
    "skills": ["Python", "Java", "C++"]
}

json_string = json.dumps(person)
print(json_string)
print(type(json_string))

# JSON string to Python dict
back_to_dict = json.loads(json_string)
print(back_to_dict)
print(type(back_to_dict))

#  dumps — dict to string (d for dict, s for string)
# loads — string to dict (l for load, s for string)

with open("profile.json", "w") as file:
    json.dump(person, file)

# Read it back and print your name from it
with open("profile.json","r")as file:
    data = json.load(file)
    print(data["name"])
    
# json.dumps() — dict to string
# json.dump() — dict to file
# json.loads() — string to dict
# json.load() — file to dict

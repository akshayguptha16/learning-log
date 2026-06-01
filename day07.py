# # write
# with open("notes.txt", "w") as file:
#     file.write("Python is fun" + "\n" + "I am learning backend development" + "\n" + "I commit code every day" + "\n")

# # read
# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

lines = [
    "Python is fun\n",
    "I am learning backend development\n",
    "I commit code every day\n"
]
with open("notes.txt", "w") as file:
    file.writelines(lines)

with open("notes.txt", "r") as file:
    content = file.readlines()

for index, line in enumerate(content):
    print(f"{index + 1}. {line.strip()}")



# with open("notes.txt", "r") as file:
#     content = file.readlines()
#     print(content)

# FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'

# with open("notes.txt", "a+") as file:
#     file.write("This is an additional line.\n")
#     content = file.readlines()
#     print(content)

try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")
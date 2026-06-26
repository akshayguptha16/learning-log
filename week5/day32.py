# # Day 32 — Decorators

# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


# import time

# # Decorator
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()          # Start timer
#         result = func(*args, **kwargs)  # Call the original function
#         end = time.time()            # End timer

#         print(f"{func.__name__} took {end - start:.2f} seconds")
#         return result

#     return wrapper


# @timer
# def slow_function():
#     time.sleep(1)
#     print("Function complete")


# slow_function()

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed automatically")

# Usage
with FileManager("test.txt", "w") as f:
    f.write("Hello from context manager!")
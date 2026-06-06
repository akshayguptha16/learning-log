# Project — User Data Explorer

# Fetches all users from https://jsonplaceholder.typicode.com/users
# Displays a menu:

# 1. List all users
# 2. Search user by name
# 3. Show user details
# 4. Save all users to JSON file
# 5. Exit

# Each menu option works correctly
# Handles all errors — connection failures, user not found, invalid input

import requests
import json



def fetch_users():

    try: 
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:   
        print(f"Error fetching users: {e}")
        return []
    

#  List all users
def list_users(users):
    for user in users:
        print(f"{user['id']} : {user['name']}")

# Search user by name
def search_user(users, name):
    for user in users:
        if user['name'].lower() == name.lower():
            return user
    return None

# Show user details
def show_user_details(user):
    if user:
        print(json.dumps(user, indent=4))
    else:
        print("user not found")

# Save all users to JSON file
def save_users_to_file(users, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(users, file, indent=4)
        print(f"Users saved to {filename}")
    except IOError as e:
        print(f"Error saving users to file: {e}")

users = fetch_users()

while True:
    print("\nMenu:")
    print("1. List all users")
    print("2. Search user by name")
    print("3. Show user details")
    print("4. Save all users to JSON file")
    print("5. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        list_users(users)
    elif choice == '2':
        name = input("Enter user name to search: ")
        user = search_user(users, name)
        if user:
            print(f"User found: {user['name']} (ID: {user['id']})")
        else:
            print("User not found.")
    elif choice == '3':
        user_id = input("Enter user ID to show details: ")
        try:
            user_id = int(user_id)
            user = next((u for u in users if u['id'] == user_id), None)
            show_user_details(user)
        except ValueError:
            print("Invalid input. Please enter a valid user ID.")
    elif choice == '4':
        filename = input("Enter filename to save users (e.g., users.json): ")
        save_users_to_file(users, filename)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        

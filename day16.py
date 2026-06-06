# Project — Contact Book

# Requirements:
# A Contact Book CLI application that:

# Stores contacts with — name, phone, email, city
# Has full CRUD operations:

# Create — add new contact
# Read — list all contacts, search by name
# Update — edit existing contact
# Delete — remove contact


# Persists data to contacts.json — loads on startup, saves on every change
# Has clean error handling throughout
# Split into functions — one per operation
# Menu system


import json
import requests

def fetch_users():

    try: 
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:   
        print(f"Error fetching users: {e}")
        return []
    


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    city = input("Enter city: ")

 # create a contact dictionary
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "city": city
    }

# append to contacts list
    contacts.append(contact)
    print("Contact added successfully!")

# save to contacts.json
    save_contacts_to_file(contacts, "contacts.json")
    
# print confirmation
    print(f"Contact {name} added successfully!")

def list_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, City: {contact['city']}")

def save_contacts_to_file(contacts, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)
        print(f"Contacts saved to {filename}")
    except IOError as e:
        print(f"Error saving contacts to file: {e}")


    print ("Welcome to the Contact Book CLI Application!")
    print("\n ----contact details----")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, City: {contact['city']}")

# menu 
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            list_contacts(contacts)
        elif choice == '3':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")








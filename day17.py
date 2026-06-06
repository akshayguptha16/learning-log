# import json
# import csv

# FILENAME = "contacts.json"


# # Load contacts from JSON file
# def load_contacts():
#     try:
#         with open(FILENAME, "r") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []


# # Save contacts to JSON file
# def save_contacts(contacts):
#     try:
#         with open(FILENAME, "w") as file:
#             json.dump(contacts, file, indent=4)
#     except IOError as e:
#         print(f"Error saving contacts: {e}")


# # Add Contact (Create)
# def add_contact(contacts):
#     name = input("Enter Name: ")

#     # Check duplicate contact
#     for contact in contacts:
#         if contact["name"].lower() == name.lower():
#             print("Contact already exists.")
#             return

#     phone = input("Enter Phone: ")
#     email = input("Enter Email: ")
#     city = input("Enter City: ")

#     contact = {
#         "name": name,
#         "phone": phone,
#         "email": email,
#         "city": city
#     }

#     contacts.append(contact)
#     save_contacts(contacts)

#     print(f"Contact '{name}' added successfully!")


# # List Contacts (Read)
# def list_contacts(contacts):
#     if not contacts:
#         print("No contacts found.")
#         return

#     print("\n--- Contact List ---")

#     for index, contact in enumerate(contacts, start=1):
#         print(
#             f"{index}. "
#             f"{contact['name']} | "
#             f"{contact['phone']} | "
#             f"{contact['email']} | "
#             f"{contact['city']}"
#         )


# # Search Contact (Read)
# def search_contact(contacts):
#     name = input("Enter name to search: ")

#     found = False

#     for contact in contacts:
#         if name.lower() in contact["name"].lower():
#             print(
#                 f"\nFound: "
#                 f"{contact['name']} | "
#                 f"{contact['phone']} | "
#                 f"{contact['email']} | "
#                 f"{contact['city']}"
#             )
#             found = True

#     if not found:
#         print("Contact not found.")


# # Update Contact
# def update_contact(contacts):
#     name = input("Enter name to update: ")

#     for contact in contacts:
#         if contact["name"].lower() == name.lower():

#             print("\nPress Enter to keep current value.")

#             new_name = input(f"Name ({contact['name']}): ")
#             new_phone = input(f"Phone ({contact['phone']}): ")
#             new_email = input(f"Email ({contact['email']}): ")
#             new_city = input(f"City ({contact['city']}): ")

#             if new_name:
#                 contact["name"] = new_name

#             if new_phone:
#                 contact["phone"] = new_phone

#             if new_email:
#                 contact["email"] = new_email

#             if new_city:
#                 contact["city"] = new_city

#             save_contacts(contacts)

#             print("Contact updated successfully!")
#             return

#     print("Contact not found.")


# # Delete Contact
# def delete_contact(contacts):
#     name = input("Enter name to delete: ")

#     for contact in contacts:
#         if contact["name"].lower() == name.lower():

#             contacts.remove(contact)

#             save_contacts(contacts)

#             print("Contact deleted successfully!")
#             return

#     print("Contact not found.")


# # Export Contacts to CSV
# def export_contacts_to_csv(contacts):
#     if not contacts:
#         print("No contacts to export.")
#         return
#     filename = "contacts_export.csv"
#     with open(filename, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "city"])
#         writer.writeheader()
#         writer.writerows(contacts)
#     print(f"Contacts exported to {filename}")


# # Main Program
# def main():

#     contacts = load_contacts()

#     print("Welcome to Contact Book CLI")

#     while True:

#         print("\n===== MENU =====")
#         print("1. Add Contact")
#         print("2. List Contacts")
#         print("3. Search Contact")
#         print("4. Update Contact")
#         print("5. Delete Contact")
#         print("6. Export Contacts to CSV")
#         print("7. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_contact(contacts)

#         elif choice == "2":
#             list_contacts(contacts)

#         elif choice == "3":
#             search_contact(contacts)

#         elif choice == "4":
#             update_contact(contacts)

#         elif choice == "5":
#             delete_contact(contacts)

#         elif choice == "6":
#             export_contacts_to_csv(contacts)

#         elif choice == "7":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please try again.")

import csv
import json 


def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_contacts(contacts):
    filename = "contacts.json"
    try:
        with open(filename, 'w') as file:
            json.dump(contacts, file, indent=4)
    except IOError as e:
        print(f"Error saving contacts to file: {e}") 



def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    city = input("Enter city: ")


    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "city": city
    }


    contacts.append(contact)
   
    save_contacts(contacts)

    print(f"Contact {name} added successfully!")

    

    
def list_contacts(contacts):
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['city']}")

    
def search_contact(contacts):
    name = input("Enter name to search:")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Contact found: {contact['name']}, {contact['phone']}, {contact['email']}, {contact['city']}") 
            return
    else:     
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete:")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact {name} deleted successfully!")
            return
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update:")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"Email ({contact['email']}): ") or contact['email']
            new_city = input(f"City ({contact['city']}): ") or contact['city']
            contact['phone'] = new_phone    
            contact['email'] = new_email
            contact['city'] = new_city
            save_contacts(contacts)
            print(f"Contact {name} updated successfully!")
            return
    else:
        print("Contact not found.")

def export_contacts_to_csv(contacts):
    if not contacts:
        print("No contacts to export.")
        return
    with open("contacts_export.csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "city"])
        writer.writeheader()
        writer.writerows(contacts)
    print("Contacts exported to contacts_export.csv")


contacts = load_contacts()
print("Welcome to the Contact Book CLI Application!")
print("\n---- Contact Details ----")
for index, contact in enumerate(contacts):
    print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, City: {contact['city']}")

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Export contacts to CSV")
    print("7. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact(contacts)
    elif choice == '2':
        list_contacts(contacts)
    elif choice == '3':
        search_contact(contacts)
    elif choice == '4':
        update_contact(contacts)
    elif choice == '5':
        delete_contact(contacts)
    elif choice == '6':
        export_contacts_to_csv(contacts)
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
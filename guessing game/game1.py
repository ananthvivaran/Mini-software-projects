import os
import re

CONTACTS_FILE = "contacts.txt"

# Function to load contacts from the file
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts

# Function to save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

# Function to validate phone number
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Function to validate email
def is_valid_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    while not is_valid_phone(phone):
        print("Invalid phone number. It must be 10 digits long.")
        phone = input("Enter phone number: ")
    
    email = input("Enter email address: ")
    while not is_valid_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter email address: ")

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

# Function to edit a contact
def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        
        phone = input("Enter new phone number: ")
        while not is_valid_phone(phone):
            print("Invalid phone number. It must be 10 digits long.")
            phone = input("Enter new phone number: ")
        contacts[index]['phone'] = phone
        
        email = input("Enter new email address: ")
        while not is_valid_email(email):
            print("Invalid email address. Please enter a valid email.")
            email = input("Enter new email address: ")
        contacts[index]['email'] = email
        
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

# Main function to run the contact manager
def contact_manager():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

# Run the contact manager
if __name__ == "__main__":
    contact_manager()

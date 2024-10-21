contacts = []

def add_contact():
    # Collect contact information from the user
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    # Create a new contact dictionary and add it to the contacts list
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully.")

def view_contacts():
    # Display all contacts with name and phone number
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    # Prompt user for search criteria
    search_term = input("Enter the name or phone number to search: ").lower()
    
    # Search for contacts matching the search term
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    # Display search results
    if not found_contacts:
        print("No contacts found.")
    else:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

def update_contact():
    # Search for a contact to update
    name_to_update = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name_to_update:
            # Update contact details
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email address: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print(f"Contact {contact['name']} updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    # Search for a contact to delete
    name_to_delete = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name_to_delete:
            contacts.remove(contact)
            print(f"Contact {contact['name']} deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        # Display menu options
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        # Get the user's choice
        choice = input("Choose an option (1-6): ")

        # Execute the corresponding function based on the user's choice
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the contact management system
main()

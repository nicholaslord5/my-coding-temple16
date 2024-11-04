contacts = {
    "1234567890": {
        "name": "Nick Lord",
        "phone": "1235557890",
        "email": "nicklord@example.com",
        "address": "1234 Five St",
        "notes": "Wrote this code"
    }
}
import re

def validate_phone(phone):
    return re.match(r"^\d{10}$", phone) is not None

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def add_contact(contacts):
    print("\nAdd a New Contact")
    name = input("Enter name: ")
    phone = input("Enter 10-digit phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address:")
    notes = input("Enter any notes:")
    
    if not validate_phone(phone):
        print("Invalid format - phone number must be 10 digits.")
        return
    if not validate_email(email):
        print("Invalid email format.")
        return

    if phone in contacts:
        print("A contact with this phone number already exists.")
        return
    
    contacts[phone] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }
    print("Success! Contact added.")

def edit_contact(contacts):
    phone = input("\nEnter the phone number of the contact you want to edit: ")
    
    if phone not in contacts:
        print("Contact not found.")
        return
    
    contact = contacts[phone]
    print(f"Editing Contact: {contact['name']}")

    name = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
    email = input(f"Enter new email (or press Enter to keep '{contact['email']}'): ") or contact['email']
    address = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
    notes = input(f"Enter new notes (or press Enter to keep '{contact['notes']}'): ") or contact['notes']
    
    if not validate_email(email):
        print("Invalid email format.")
        return
    
    contacts[phone] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "notes": notes
    }
    print("Success! contact updated.")

def delete_contact(contacts):
    email = input("\nEnter the email of the contact you want to delete: ")
    
    if email in contacts:
        confirm = input(f"Are you sure you want to delete {contacts[email]['name']}? (y/n): ")
        if confirm.lower() == 'y':
            del contacts[email]
            print("Success! Contact deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    search_term = input("\nEnter a name, phone number, or email to search: ").lower()
    found = False
    
    for contact in contacts.values():
        if (search_term in contact['name'].lower() or
            search_term in contact['phone'] or
            search_term in contact['email'].lower()):
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print(f"Notes: {contact['notes']}")
            found = True
    
    if not found:
        print("No contacts found with that search term.")

def display_all_contacts(contacts):
    if not contacts:
        print("\nNo contacts available.")
        return
    
    print("\nAll Contacts:")
    for contact in contacts.values():
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")

def export_contacts(contacts, filename="contacts.txt"):
    try:
        with open(filename, 'w') as file:
            for contact in contacts.values():
                file.write(f"Name: {contact['name']}\n")
                file.write(f"Phone: {contact['phone']}\n")
                file.write(f"Email: {contact['email']}\n")
                file.write(f"Address: {contact['address']}\n")
                file.write(f"Notes: {contact['notes']}\n")
                file.write("\n---\n")
        print(f"Success ! Contacts exported to {filename}.")
    except Exception as e:
        print("Error exporting contacts:", e)

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Quit")

def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            edit_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            display_all_contacts(contacts)
        elif choice == "6":
            export_contacts(contacts)
        elif choice == "7":
            print("Now leaving the Contact Management System. Goodbye!")
            break
        else:
            print("Oops! invalid choice. Please try again.")

if __name__ == "__main__":
    main()

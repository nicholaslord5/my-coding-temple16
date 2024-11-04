This Contact Management System is a Python command-line application that allows users to easily manage their contacts. 
With this application, you can add, edit, delete, search, display, and export contacts to a text file. 

###

Features
Add a New Contact: Add a new contact with details like name, phone number, email address, address, and notes.
Edit an Existing Contact: Update details of an existing contact.
Delete a Contact: Delete a contact from the system.
Search for a Contact: Find and display a contact by name, phone number, or email.
Display All Contacts: Show all contacts stored in the system.
Export Contacts: Save all contacts to a text file.
Import Contacts (Bonus): Load contacts from a text file and add them to the system.
User-friendly Command-Line Interface: Navigate easily through a simple text-based menu.
Input Validation: Ensures that phone numbers and email addresses are correctly formatted.
Error Handling: Manages unexpected issues during execution, such as file errors.

###

The project uses the following structure:

Contacts: A nested dictionary where each contact’s details are stored, using the contact’s phone number as the unique identifier.
Functions: Each menu option has a separate function for modularity and readability.
Menu: The main menu displays options to the user and calls the appropriate functions based on user input.

###
To run this program, you need:

Python 3.x installed on your system. You can download it from python.org.

To start the Contact Management System, open a terminal or command prompt in the project folder and run: python contact_management_system.py

###

Start the program and follow the on-screen menu options.
Choose an option by typing the number associated with the action (for example, type 1 to add a new contact).
Follow prompts for each action, entering contact details and info.
Exit the program by selecting option 7 in the menu.

###

Here’s what using the Contact Management System looks like:

Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Quit

Select option: 1
Enter name: Nick Lord
Enter 10-digit phone number: 1235555555
Enter email address: nicklord@example.com
Enter address: 1234 Five St
Enter any notes: Wrote this code
Contact added successfully!

###

Each function handles a specific action:

add_contact(): Adds a new contact after validating inputs.
edit_contact(): Modifies an existing contact’s details.
delete_contact(): Deletes a contact from the dictionary.
search_contact(): Finds contacts matching a search term.
display_all_contacts(): Lists all contacts.
export_contacts(): Saves contacts to a text file.

####

The application handles various errors, such as Input errors: Checks for valid phone number and email format.

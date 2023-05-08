#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##### contact_book = {}

# Define a function to add a new contact
def add_contact(name, phone):
    # Check if the name already exists in the contact book
    if name in contact_book:
        # Print an error message
        print("This name already exists in the contact book.")
    else:
        # Add the name and phone number as a key-value pair to the dictionary
        contact_book[name] = phone
        # Print a success message
        print("Contact added successfully.")

# Define a function to delete an existing contact
def delete_contact(name):
    # Check if the name exists in the contact book
    if name in contact_book:
        # Delete the name and phone number from the dictionary
        del contact_book[name]
        # Print a success message
        print("Contact deleted successfully.")
    else:
        # Print an error message
        print("This name does not exist in the contact book.")

# Define a function to update an existing contact
def update_contact(name, phone):
    # Check if the name exists in the contact book
    if name in contact_book:
        # Update the phone number for the given name in the dictionary
        contact_book[name] = phone
        # Print a success message
        print("Contact updated successfully.")
    else:
        # Print an error message
        print("This name does not exist in the contact book.")

# Define a function to display all the contacts
def display_contacts():
    # Check if the contact book is empty
    if not contact_book:
        # Print an error message
        print("The contact book is empty.")
    else:
        # Print all the key-value pairs in the dictionary
        for name, phone in contact_book.items():
            print(name, ":", phone)

# Define a function to display the menu options
def display_menu():
    print("Welcome to the contact book.")
    print("Please choose an option:")
    print("1. Add a new contact")
    print("2. Delete an existing contact")
    print("3. Update an existing contact")
    print("4. Display all the contacts")
    print("5. Exit")

# Define a main function to run the program
def main():
    # Display the menu options
    display_menu()
    # Loop until the user chooses to exit
    while True:
        # Get the user's choice as an integer
        choice = int(input("Enter your choice: "))
        # Check if the choice is valid
        if choice in range(1, 6):
            # Perform different actions based on the choice
            if choice == 1:
                # Get the name and phone number from the user
                name = input("Enter the name: ")
                phone = input("Enter the phone number: ")
                # Call the add_contact function with the name and phone number as arguments
                add_contact(name, phone)
            elif choice == 2:
                # Get the name from the user
                name = input("Enter the name: ")
                # Call the delete_contact function with the name as an argument
                delete_contact(name)
            elif choice == 3:
                # Get the name and phone number from the user
                name = input("Enter the name: ")
                phone = input("Enter the new phone number: ")
                # Call the update_contact function with the name and phone number as arguments
                update_contact(name, phone)
            elif choice == 4:
                # Call the display_contacts function with no arguments
                display_contacts()
            elif choice == 5:
                # Break out of the loop and exit the program
                break
            # Display a blank line for readability
            print()
        else:
            # Print an error message for invalid choice
            print("Invalid choice. Please try again.")
            # Display a blank line for readability
            print()

# Call the main function to run the program
main()


# In[ ]:





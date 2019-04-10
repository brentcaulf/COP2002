#!/usr/bin/env python3

import csv

# a file in the current directory
FILENAME = "contacts.csv"

# displays the program title
def display_title():
    print("Contact Manager")
    print()

# displays the menu and command choices
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program")
    print()

# writes to the contacts file
def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

# reads from the contacts file creating a list
def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

# uses the contacts list to display all of the contacts name and command number
def list_contacts(contacts):
    number = 0
    for row in contacts:
        number += 1
        print(str(number) + ". " + row[0])
    print()

# views information for a single contact using their command number
def view_contact():
    contacts_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        
        for row in reader:
            contacts_list.append(row)
        # gets the contact number to view
        row = (int(input("Enter contact number: ")))
        # checks to make sure it's a valid number
        if row < 1 or row > len(contacts_list):
            print("Invalid contact number.")
        else:
            # subtract one from the number selection to match the list
            row = row - 1
            print()
            print("Name: " + contacts_list[row][0])
            print("Email: " + contacts_list[row][1])
            print("Phone: " + contacts_list[row][2])
    print()

# add a contact and input their name, email, and phone...
# then add it to the list and write it to the file
def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

# deletes a contact using a valid number
def delete_contact(contacts):
    index = int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("Invalid contact number.")
    else:
        contact = contacts.pop(index - 1)
        write_contacts(contacts)
        print(contact[0] + " was deleted.\n")

# main function
def main():
    display_title()
    display_menu()

    # read the contacts from CSV file when program starts and sets a list variable
    contacts = read_contacts()

    while True:
        command = input("Command: ")
        if command == "list":
            list_contacts(contacts)
        elif command == "view":
            view_contact()
        elif command == "add":
            add_contact(contacts)
        elif command == "del":
            delete_contact(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    print("Bye!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import csv

# a file in the current directory
FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)   

#reads the contacts file
#if it cant find one it displays an error and creates a new one
def read_contacts():
    try:
        contacts = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        print("Starting new contacts file...\n")
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        return contacts

def display(contacts):
    if len(contacts) == 0:
        print("There are no contacts in the list.\n")
        return
    else:
        i = 1
        for row in contacts:
            print(str(i) + ". " + row[0])
            i += 1
        print()

def add(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(contact[0] + " was added.")   
    print()

#view a contact entry and validate input
def view(contacts):
    if (len(contacts) == 0):
        print("No contacts available. Please add a contact before using this command.\n")
    else:
        while True:
            try:
                number = int(input("Number: "))
            #if input isn't an integer, display error and continue loop
            except ValueError:
                print("Invalid integer. Please try again.\n")
                continue
            #if input isn't a valid contact number display error
            if number < 1 or number > len(contacts):
                print("Invalid contact number. Please try again.\n")
            else:
                break
        contact = contacts[number-1]
        print("Name: " + contact[0])
        print("Email: " + contact[1])
        print("Phone: " + contact[2])
        print()

#delete a contact entry and validate input      
def delete(contacts):
    if (len(contacts) == 0):
        print("No contacts available. Please add a contact before using this command.\n")
    else:
        while True:
            try:
                number = int(input("Number: "))
            #if input isn't an integer, display error and continue loop
            except ValueError:
                print("Invalid integer. Please try again.\n")
                continue
            #if input isn't a valid contact number display error
            if number < 1 or number > len(contacts):
                print("Invalid contact number.\n")
            else:
                break
        contact = contacts.pop(number-1)
        print(contact[0] + " was deleted.\n")
        write_contacts(contacts)
      
def display_title():
    print("Contact Manager")
    print()

def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("exit - Exit program")
    print()    

def main():
    contacts = read_contacts()
    display_title()    
    display_menu()    
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts)
        elif command == "view":
            view(contacts)
        elif command == "add":
            add(contacts)
        elif command == "del":
            delete(contacts)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

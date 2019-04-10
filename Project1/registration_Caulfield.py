#!/usr/bin/env python3

# display title
print("Student Registration")
print()

# get first name input
first_name = input("First name: ")

# get last name input
last_name = input("Last name: ")

# get birth year input
birth_year = input("Birth year: ")

# display information
print()
print("Welcome " + first_name + " " + last_name + "!")
print("Your registration is complete.")
print("Your temporary password is: " + first_name + "*" + birth_year)

print()
input('Press ENTER to exit')

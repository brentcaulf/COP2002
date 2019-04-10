#!/usr/bin/env python3

"""
Project Statement
The guessing game has four errors. Find and correct the errors so that
the user can set an upper limit to the range of numbers, it gets a random
number in that range, and allows the user to guess until correct. It should
display 'too high' or 'too low' hints.
-------------------------------------------------------------------------
When you fix the program, upload the working program and list, as comments,
the errors you found and fixed.
Error 1: syntax error in the main functions declaration. fixed by adding :
Error 2: error where argument (limit) wasn't passed in
Error 3: assignment error. set count to 1 since the final guess will need to count also
Error 4: too high check was returning true if it was equal to the number
"""

import random

def display_title():
    print("Guess the number!")
    print()

def set_limit():
    print("Enter the upper limit for the range of numbers: ")
    limit = int(input())
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    count = 1 #error 3
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    while True:
        guess = int(input("Your guess: "))        
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number: #error 4
            print("Too high.")
            count += 1
        elif guess == number:
            print("You guessed it in " + str(count) + " tries.\n")
            return


def main(): #error 1
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = set_limit()
        play_game(limit) #error 2
        again = input("Play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


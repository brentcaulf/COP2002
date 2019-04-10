#!/usr/bin/env python3

#Display Title
print("Change Calculator")
print()

#Start loop
more = "y"
while more.lower() == "y":
    #get dollar amount from user
    dollar_amount = float(input("Enter dollar amount (for example, .56, 7.85): "))

    #declare variables
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    #calculate number of quarters by seeing if it divides evenly
    quarters_mod = round(dollar_amount % .25, 2)
    if quarters_mod == 0:
        quarters = dollar_amount / .25
    else:
        #if there is a remainder then set quarters here and continue calculation
        quarters = dollar_amount / .25
        #see if dimes divides evenly into the remainder and if it does set it
        dimes_mod = round(quarters_mod % .1, 2)
        if dimes_mod == 0:
            dimes = quarters_mod / .1
        else:
            #if dimes has a remainder than calculate nickels
            dimes = quarters_mod / .1
            nickels_mod = round(dimes_mod % .05, 2)
            if nickels_mod == 0:
                nickels = dimes_mod / .05
            else:
                #if there is a remainder from the nickels then calculate pennies
                nickels = dimes_mod / .05
                pennies = nickels_mod / .01
                

    #display results
    print("Quarters: ", int(quarters))
    print("Dimes: ", int(dimes))
    print("Nickels: ", int(nickels))
    print("Pennies: ", int(pennies))

    #check to see if program should run again
    print()
    more = input("Continue? (y/n): ")
    while (more != "y" and more != "n"):
        print("Please enter y or n")
        more = input("Continue? (y/n): ")
    print()

print("Bye!")

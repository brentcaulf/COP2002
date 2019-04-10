#!/usr/bin/env python3

#get valid input function
def getInput():
    while True:        
        try:
            num = int(input("Please enter a integer between 1 and 5,000: "))
            if num < 0:
                print("Prime numbers cannot be negative. Please try again.")
                continue
        except ValueError:
            print("That's not a int! Please try again.")
            continue
        else:
            return num
            break

        
#print factors function
def printFactors(num):
    #Prime numbers must be greater than 1
    if num > 1:
        for i in range(2,num):
            #If mod is 0 then not a prime number
            if (num % i) == 0:
                #Calculate and print factors for non-prime numbers
                print("The factors of your number are:")
                numFactors = 0
                for i in range(1, num + 1):
                    if num % i == 0:
                        print(i)
                        numFactors += 1
                print(num, "is NOT a prime number.")
                print("It has ", numFactors, " factors.")
                break
        #Otherwise it IS a prime number
        else:
            #Calculate and print factors for prime numbers
            print("The factors of your number are:")
            numFactors = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    print(i)
            print(num, "is a prime number.")
            

#main function
def main():
    #Display Title
    print("Prime Number Checker")
    print()

    #Start main loop
    choice = "y"
    while choice.lower() == "y":
        #Call getInput function to get a valid number
        num = getInput()
        #Call printFactors function which determines if it's prime or not,
        #then calculates and displays the factors with relevant message.
        printFactors(num)

        #Check if user wants to continue
        print()
        choice = input("Try again? (y/n): ")
        while (choice != "y" and choice != "n"):
            print("Please enter y or n")
            choice = input("Continue? (y/n): ")
        print()


#Calls main function
if __name__ == "__main__":
    main()

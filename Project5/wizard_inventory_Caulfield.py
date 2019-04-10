def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(item_list):
    i = 1
    for item in item_list:
        print(str(i) + ". " + item)
        i += 1
    print()

def grab(item_list):
    if len(item_list) == 4:
        print("You can't carry any more items. Drop something first.")
    else:
        item = input("Name: ")
        item_list.append(item)
        print(item + " was added.")
    print()

def edit(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.\n")
    else:
        number -= 1
        item_list[number] = input("Updated name: ")
        number += 1
        print("Item number " + str(number) + " was updated.")
    print()

def drop(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.\n")
    else:
        item = item_list.pop(number-1)
        print(item + " was dropped.\n")
    print()

def main():
    item_list = ["wooden staff", "wizard hat", "cloth shoes"]

    print("The Wizard Inventory program")
    print()

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show(item_list)
        elif command.lower() == "grab":
            grab(item_list)
        elif command.lower() == "edit":
            edit(item_list)
        elif command.lower() == "drop":
            drop(item_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    print("Bye!")
            

if __name__ == "__main__":
    main()

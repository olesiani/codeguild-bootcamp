import sys
contacts = {}
anotherstorage = []

def adding():
    anotherstorage = []
    file = open('People.txt', 'r')
    lines = file.readlines()
    file.close()
    file = open('People.txt', 'a')
    name = input("Enter the name: ")
    for line in lines:
        if name in line:
            anotherstorage.append(1)
    while 1 in anotherstorage:
        name = input("That name already exists. Enter a unique name: ")
        anotherstorage = []
        for line in lines:
            if name in line:
                anotherstorage.append(1)
            
    phonenumber = input("Enter the phone number: ")
    contacts[name] = phonenumber
    for contact, value in contacts.items():
        file.write(contact)
        file.write(" - ")
        file.write(value)
        file.write("\n")
    file.close()
    contacts.clear()
    print(name, "was added to the list.")
    
needtostore = []
searchstore = []
updatestore = []
print("""Welcome to the address book!
Your options are: 
-add: adds a person and their phone number
-delete: deletes a person (along with their phone number)
-search: searches for a person in the address book, and displays their phone number.
-list: lists ALL the people in the address book and their corresponding phone numbers.
-update: updates the phone number for a specific person.
-clear: deletes everything from the address book. Use caution, as this is irreversible.
-quit: quits out of the app. 
""")

while True:
    choice = input("Enter address book command: ")
    if choice == "quit":
        print("Thank you for using the address book. Goodbye.")
        break
    elif choice == "add":
        adding()
                    
    elif choice == "delete":
        file = open('People.txt', 'r')
        lines = file.readlines()
        file.close()
        persontodelete = input("Enter the name of the person to remove: ")
        for line in lines:
            if persontodelete in line:
                needtostore.append("found")
        while "found" not in needtostore:
            persontodelete = input("Oops! That person isn't there. Enter another person to remove: ")
            needtostore = []
            for line in lines:
                if persontodelete in line:
                    needtostore.append("found")
        file = open('People.txt', 'w')
        for line in lines:
            if persontodelete not in line:
                file.write(line)
        file.close()
        print(persontodelete, "has been deleted.")
    elif choice == "search":
        searchstore = []
        file = open('People.txt', 'r')
        lines = file.readlines()
        file.close()
        persontofind = input("Enter the name of the person to search for: ")
        for line in lines:
            if persontofind in line:
                print(line)
                searchstore.append(1)
        if 1 not in searchstore:
            print("No such person in directory. ")
            
        


    elif choice == "list":
        file = open('People.txt', 'r')
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()

    elif choice == "update":
        contacts.clear()
        file = open('People.txt', 'r')
        lines = file.readlines()
        file.close()
        persontoupdate = input("Enter the name of the person who's phone number to update: ")
        for line in lines:
            if persontoupdate in line:
                updatestore.append(1)
        while 1 not in updatestore:
            persontoupdate = input("Oops! That person doesn't exist. Enter another one to update: ")
            updatestore = []
            for line in lines:
                if persontoupdate in line:
                    updatestore.append(1)
        newnumber = input("Enter new phone number: ")
        contacts[persontoupdate] = newnumber
        file = open('People.txt', 'w')
        space = " "
        personplusspace = persontoupdate + space
        for line in lines:
            if personplusspace not in line:
                file.write(line)
            if personplusspace in line:
                for contact, value in contacts.items():
                    file.write(contact)
                    file.write(" - ")
                    file.write(value)
                    file.write("\n")
        file.close()
        contacts.clear()
        print(persontoupdate + "'s phone number has been updated.")
    elif choice == "clear":
        areyousure = input("""Are you SURE you want to delete EVERYTHING from the address book?
There are no returns!
Type 'y' for yes and 'n' for no: """)
        if areyousure == "y":
            file = open('People.txt', 'w')
            file.close()
            print("Address book was cleared.")
    
    else:
        print("I don't know that command. Try again: ")
    

from roomClass import room
import databaseManagement
import sys
import databaseManagement

def opMenu():
    print("----------\n1 - Reserve a new room\n2 - Show all rooms\n3 - Edit reservation\n4 - Quit")
    return(int(input()))

print("Welcome to Flounder Lodgings! Select an option: ")
roomList = databaseManagement.initDB()
while(True):
    choice = opMenu()
    if choice == 1:
        print("----------\nThe following rooms are vacant: ")
        for i in roomList:
            roomList[i].printInfo()
    elif choice == 2:
        for i in roomList:
            roomList[i].printInfo(True)
    elif choice == 3:
        roomNo = input("Which room are you staying in? ")
        newTime = [str(x) for x in input("Which date would you like to schedule for (MM/DD/YYYY) ")]
        roomList[roomNo.upper()].changeTime(newTime)
    elif choice == 4:
        print("Thank you for considering us for your lodging needs!")
        break
    else:
        print("Invalid choice, try again")



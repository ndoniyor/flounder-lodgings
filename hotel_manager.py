from room_class import Room, RoomStatus
import database_management
import sys

print("Welcome to Flounder Lodgings! Select an option: ")
roomList = database_management.initDB()
while(True):
    choice = input(("----------\n1 - Search for room\n2 - Check in\n3 - Check out\n4 - Print all rooms\nx - Quit"))
    if choice == '1':
        input("How many beds ")
    #elif choice == '2':
        
    # elif choice == '3':
    elif choice == '4':
        print("----------\nThe following rooms are vacant: ")
        for room in roomList:
            print(room)
    elif choice == 'x':
        print("Thank you for considering us for your lodging needs!")
        break
    else:
        print("Invalid choice, try again")



from roomClass import Room
import databaseManagement
import sys
import databaseManagement

# This file is called vacancy_checker but it seems like it's just the main file (doing more than checking vacancy).
# A more appropriate filename could just be "manager.py" or "hotel_manager.py"
# Also think about what a hotel manager does:
# 1. Finds room
#     a. Guest has certain room requirements such as: "1 Bed, under $300 per night"
#     b. You try to find a room that fits those requirements.
# 2. Checks people into rooms
#     a. Find an empty room
#     b. Find out what guest will be staying there
#     c. Mark it as full
# 3. Check people out
#     a. Check to see if their checkout time is here
#     b. Remove the guest from the occupied list
#     c. Tell room service to clean room
#     d. Mark it as vacant after its been cleaned

# Those points can be their own function. You need to break up your thinking in that way.
# There are steps that belong together so you put them in a function.
# This will not only make your code more modular but it will make your classes and
# other functions that much cleaner. Your functions and function calls should read like English.



def opMenu():
    print("----------\n1 - Reserve a new room\n2 - Show all rooms\n3 - Edit reservation\n4 - Quit")
    return(int(input()))


print("Welcome to Flounder Lodgings! Select an option: ")
roomList = databaseManagement.get_dummy_roomlist()
while(True):
    choice = opMenu()
    if choice == 1:
        print("----------\nThe following rooms are vacant: ")
        for room in roomList:
            print(room)
    elif choice == 2:
        for room in roomList:
            print(room)
    elif choice == 3:
        # This doesn't read like English. A refactored version can be:
        # room = find_vacant_room(some requirements that guest has)
        # room.new_stay(guest, checkout_time)
        roomNo = input("Which room are you staying in? ") # Not guest's job to know what room they're staying in.
        newTime = [str(x) for x in input(
            "Which date would you like to schedule for (MM/DD/YYYY) ")]
        roomList[roomNo.upper()].changeTime(newTime)
    elif choice == 4:
        print("Thank you for considering us for your lodging needs!")
        break
    else:
        print("Invalid choice, try again")

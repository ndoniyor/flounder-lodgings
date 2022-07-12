import os
from roomClass import room

def initDB():
    roomList = dict()
    roomInfo = list()
    database = open('roomDB.txt','r+')
    if (os.path.getsize('roomDB.txt')!=0):
        print("Importing existing room database...")
        for line in database:
            info = str(line).strip('\n').split(' ')
            roomNo = info[0]
            roomInfo.append(info[1])
            roomInfo.append(info[2])
            roomPrice = info[3]
            roomStatus = info[4]
            roomTime = info[5]
            roomList[roomNo]=(room(roomNo,roomInfo,roomPrice,roomStatus,roomTime))
    else:
        print("Database is empty.")
        return None
    return roomList 
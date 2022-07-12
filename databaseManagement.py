import os
import sqlite3
from roomClass import Room, RoomStatus

from datetime import datetime

def initDB():
    roomList = dict()
    database = sqlite3.connect('roomDB.db')
    cursor = database.cursor()
    cursor.execute("INSERT INTO rooms VALUES ('1A','1BED',500,'VACANT', '')")
    cursor.execute("INSERT INTO rooms VALUES ('1A','1BED',500,'FULL','2022-07-31')")
    database.commit()
    print("hello")
    print(cursor.execute("SELECT roomNo, roomInfo, roomPrice, roomStatus, roomTime FROM rooms").fetchall())
    # if (os.path.getsize('roomDB.txt')!=0):
    #     print("Importing existing room database...")
    #     for line in database:
    #         info = str(line).strip('\n').split(' ')
    #         roomNo = info[0]
    #         roomInfo.append(info[1])
    #         roomInfo.append(info[2])
    #         roomPrice = info[3]
    #         roomStatus = info[4]
    #         roomTime = info[5]
    #         roomList[roomNo]=(room(roomNo,roomInfo,roomPrice,roomStatus,roomTime))
    # else:
    #     print("Database is empty.")
    #     return None
    # return roomList 

def get_dummy_roomlist():
    room_list = []
    room_list.append(Room('1A', '1B 1BR', 500, RoomStatus.VACANT))
    room_list.append(Room('1B', '1B 1BR', 500, RoomStatus.UNAVAILABLE, datetime.now()))
    return room_list

initDB()
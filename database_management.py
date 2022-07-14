import os
import sqlite3
from room_class import Room
from datetime import datetime

database = sqlite3.connect('roomdb.db')
cursor = database.cursor()
def init_DB():
    roomList = dict()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM rooms WHERE roomNo = '1A')") #fix so that it detects if db is empty
    if(cursor.fetchone()==(1,)):
        return 0
    for row in cursor.execute('SELECT * from rooms ORDER BY roomNo'):
        roomNo, roomInfo, roomPrice, roomStatus, roomDate = row
        roomList[roomNo] = roomNo, roomInfo, roomPrice, roomStatus, roomDate

def search_query(bed_count, price_range, date_range):
    valid_rooms = list()
    cursor.execute("SELECT * from rooms WHERE roomStatus = 'VACANT' ORDER BY roomNo")
    for roomNo, roomInfo, roomPrice, roomStatus, roomDate in cursor.fetchall(): 
        user_bed_count, user_price_ceiling, user_date_range = input("Enter your desired bed count, price ceiling and date range: ")
        user_bed_count = str(user_bed_count) + "BED"
        #! for following line need to add comparator to return items that match the range
        cursor.execute(f"SELECT * from rooms WHERE roomInfo = {user_bed_count} AND roomPrice <= {user_price_ceiling} AND ORDER BY roomNo")   
    return valid_rooms
roonList = init_DB()
valid = search_query(2,3,4)
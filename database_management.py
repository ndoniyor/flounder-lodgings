import os
import sqlite3
from room_class import Room
import datetime

database = sqlite3.connect('roomdb.db')
cursor = database.cursor()

def update_listings():
    today = datetime.date.today()
    tomorrow = (today + datetime.timedelta(days=1))
    cursor.execute(f"update rooms set roomStatus = 'CLEANING', roomTime = '{tomorrow.strftime('%Y-%m-%d')}' where roomTime = '{today.strftime('%Y-%m-%d')}'")
    database.commit()
    cursor.execute(f"update rooms set roomStatus = 'VACANT', roomTime = '' where roomTime < '{today.strftime('%Y-%m-%d')}'")
    database.commit()
    #cursor.execute("select * from rooms order by roomNo")
    #print(cursor.fetchall())

def init_DB():
    update_listings()
    roomList = dict()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM rooms WHERE roomNo = '1A')") #fix so that it detects if db is empty
    if(cursor.fetchone()==(1,)):
        return
    for row in cursor.execute('SELECT * from rooms ORDER BY roomNo'):
        roomNo, roomInfo, roomPrice, roomStatus, roomDate = row
        roomList[roomNo] = roomInfo, roomPrice, roomStatus, roomDate
    return roomList

def search_query(bed_count, price_range, date_range):
    valid_rooms = list()
    cursor.execute(f"SELECT * from rooms WHERE roomInfo >= {bed_count} AND roomPrice <= {price_range} AND (roomStatus = 'VACANT' OR roomTime < {date_range});")
    for i in cursor.fetchall():
        valid_rooms.append(i)
    return valid_rooms

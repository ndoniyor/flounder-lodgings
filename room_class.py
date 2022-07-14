from enum import Enum
class RoomStatus(Enum):
    UNAVAILABLE = 0
    VACANT = 1
    CLEANING = 2
class Room:
    def __init__(self, number, info, price, status, time):
        self.room_number = number
        self.bed_count = info
        self.price = price
        self.status = status
        self.checkout_time = time

    def __str__(self):
        if self.status == RoomStatus.VACANT:
            return (f'{self.room_number} - {self.bed_count} | {self.price}/night')
        elif self.status == RoomStatus.UNAVAILABLE:
            return("Unavailable")
        else:
            return(f'{self.room_number} - {self.info} ${self.price}/night {self.status} {self.checkout_time}')
    def changeStatus(self,status):
        self.status = status
    def changeTime(self,time):
        self.time = time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __sub__(self,other):
        if(self.year>=other.year and self.month>=other.month and self.day>other.day):
            return True
        else:
            return False
    # def __invert__(self):
    #     values = []
    #     values.extend([self.year,self.month,self.day])
    #     return values

    
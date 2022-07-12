from enum import Enum

class RoomStatus(Enum):
    UNAVAILABLE=0
    VACANT = 1
    CLEANING_NEEDED=2

class Room:
    def __init__(self, number, info, price, status, time=None):
        self.room_number = number
        self.info = info # What info? Your variables need to be more descriptive
        self.price = price
        self.status = status
        self.checkout_time = time

    def __str__(self):
        if self.status == RoomStatus.VACANT:
            return (f'{self.room_number} - {self.info} ${self.price}/night')
        elif self.status == RoomStatus.UNAVAILABLE:
            return ("Unavailable")
        else:
            return(f'{self.room_number} - {self.info} ${self.price}/night {self.status} {self.checkout_time}')


    
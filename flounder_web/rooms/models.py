from django.db import models
from datetime import date
# Create your models here.
class Room(models.Model):
    room_number = models.TextField()
    bed_count = models.IntegerField()
    price = models.IntegerField()
    status = models.TextField()
    checkout_time = models.DateField(default=date.today)

    def __str__(self):
        return "Room " + self.room_number

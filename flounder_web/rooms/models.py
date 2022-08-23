from django.db import models

# Create your models here.
class Room(models.Model):
    room_number = models.IntegerField()
    bed_count = models.IntegerField()
    price = models.IntegerField()
    status = models.TextField()
    checkout_time = models.DateField()

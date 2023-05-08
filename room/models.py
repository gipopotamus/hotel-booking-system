from django.db import models
from django.urls import reverse


class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('king', 'King')
    )

    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.IntegerField()
    room_image = models.ImageField(upload_to='room_images/', height_field=None, width_field=None, max_length=None,
                                   default='0.jpeg')

    def __str__(self):
        return self.room_number

    # def get_absolute_url(self):
    #     return reverse('Room', kwargs={'room_id': self.pk})


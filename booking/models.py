from django.db import models

from django.db import models
from room.models import Room
from guest.models import Guest


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room} - {self.guest} ({self.check_in} - {self.check_out})'

    def get_total_payment(self):
        nights = (self.check_out - self.check_in).days
        return nights * self.room.price
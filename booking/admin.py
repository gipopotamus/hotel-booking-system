from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest', 'room', 'check_in', 'check_out', 'is_paid')
    search_fields = ('id',)


admin.site.register(Booking, BookingAdmin)

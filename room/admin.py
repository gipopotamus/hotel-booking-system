from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price', 'room_image')
    list_filter = ('room_number',)
    search_fields = ('room_number', 'room_type')
    ordering = ('room_number',)


admin.site.register(Room, RoomAdmin)

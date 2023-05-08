from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Room


class RoomListView(TemplateView):
    model = Room
    template_name = 'base/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_types = Room.ROOM_TYPES
        rooms = [Room.objects.filter(room_type=room_type[0]).first() for room_type in room_types]
        context['rooms'] = rooms
        for i in rooms:
            print(i.room_image)
        return context


class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'

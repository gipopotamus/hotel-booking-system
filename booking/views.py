from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib import messages
from .models import Booking, Room
from .forms import BookingForm


class BookingDetailView(DetailView):
    model = Booking


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/book_room.html'
    login_url = '/guest/login'
    redirect_field_name = 'index'

    def form_valid(self, form):
        room_type = form.cleaned_data.get('room_type')
        check_in = form.cleaned_data.get('check_in')
        check_out = form.cleaned_data.get('check_out')

        available_rooms = Room.objects.filter(room_type=room_type).exclude(
            booking__check_in__lte=check_out, booking__check_out__gte=check_in)

        if not available_rooms:
            messages.error(self.request, 'No available rooms of selected type.')
            return redirect('booking:booking_create')

        room = available_rooms.first()

        guest = self.request.user
        booking = form.save(commit=False)
        booking.room = room
        booking.guest = guest
        booking.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking:booking_confirm', kwargs={'pk': self.get_context_data()['booking'].pk})


class BookingConfirmView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        booking = Booking.objects.get(pk=kwargs['pk'])
        context = {'booking': booking}

        return render(request, 'booking/booking_confirm.html', context)


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking_list')
    template_name = 'booking/booking_delete.html'

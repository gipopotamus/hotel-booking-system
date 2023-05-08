from django import forms
from .models import Booking, Room


class BookingForm(forms.ModelForm):
    room_type = forms.ChoiceField(
        choices=Room.ROOM_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ('room_type', 'check_in', 'check_out')

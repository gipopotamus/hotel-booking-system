from django.urls import path
from .views import BookingCreateView, BookingConfirmView, BookingDeleteView

app_name = 'booking'

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking_create'),
    path('confirm/<int:pk>/', BookingConfirmView.as_view(), name='booking_confirm'),
    path('delete/<int:pk>/', BookingDeleteView.as_view(), name='booking_delete'),
]

from django.urls import path
from .views import ReviewCreateView, ReviewUpdateView, ReviewListView, ReviewDeleteView

app_name = 'reviews'

urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),
    path('create/', ReviewCreateView.as_view(), name='review_create'),
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='review_edit'),
    path('delete/', ReviewDeleteView.as_view(), name='review_delete'),
]

from django.urls import path
from . import views

app_name = 'guest'

urlpatterns = [
    path('signup/', views.GuestRegisterView.as_view(), name='signup'),
    path('login/', views.GuestLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_home/', views.UserHomeView.as_view(), name='user_home'),
]

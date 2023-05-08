from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('email', 'first_name', 'last_name')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = Guest
        fields = ('email', 'password')

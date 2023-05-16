from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from booking.models import Booking
from guest.forms import RegistrationForm, LoginForm
from guest.models import Guest


class GuestRegisterView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("guest:user_home")
    template_name = "guests/registration.html"

    def get_success_url(self):
        return reverse_lazy('guest:user_home')


class GuestUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Guest
    fields = ['name', 'email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('user_home')

    def form_valid(self, form):
        guest = form.save(commit=False)
        guest.user = self.request.user
        guest.save()
        return super().form_valid(form)


class GuestLoginView(LoginView):
    form_class = LoginForm
    template_name = 'guests/login.html'
    success_url = reverse_lazy("user_home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('guest:user_home')


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('homepage')


@method_decorator(login_required, name='dispatch')
class UserHomeView(generic.View):
    def get(self, request):
        user_bookings = Booking.objects.filter(guest=self.request.user)
        context = {
            'bookings': user_bookings
        }
        return render(request, 'guests/user_home.html', context)

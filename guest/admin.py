from django.contrib import admin

from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(Guest, GuestAdmin)

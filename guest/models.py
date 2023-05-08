from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .managers import CustomUserManager


class Guest(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """ Return string representation of our user """
        return self.email



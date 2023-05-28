from django.db import models
from guest.models import Guest


class Review(models.Model):
    user = models.ForeignKey(Guest, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

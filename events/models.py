from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="No description provided")
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events') # Associate event with the creator
    capacity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_past_due(self):
        return self.date_time < timezone.now()

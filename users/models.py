from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_attendee = models.BooleanField(default=True)
    is_organizer = models.BooleanField(default=False)

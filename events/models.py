from django.db import models

from users.models import CustomUser


# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    place_address = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2)
    date = models.DateTimeField(auto_now=True)

class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
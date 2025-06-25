from django.db import models

from users.models import CustomUser


# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True) # Non dovrebbe essere necessario
    name = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    place_address = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(auto_now=True)
    organizer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organizer_id')
    registration = models.ManyToManyField(to=CustomUser)

# class Registration(models.Model):
#     registration = models.ManyToManyField(
#
#     )
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
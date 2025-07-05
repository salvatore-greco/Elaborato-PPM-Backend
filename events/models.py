from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import constraints
from django.utils import timezone
from users.models import CustomUser
import uuid


# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True) # Non dovrebbe essere necessario
    name = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    place_address = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5, validators=[MinValueValidator(Decimal('0.0'))])
    date = models.DateTimeField(default=timezone.now)
    organizer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='event_organizer')
    event_registration = models.ManyToManyField(to=CustomUser, through='Registration')
    description = models.CharField(max_length=300)
    class Meta:
        permissions = [
            ("can_register", "Determine whether a user can register"),
            ("view_own_registration", "Determine whether a user can view his own registration"),
            ("view_attendee", "Determine whether a user can view attendee at their own events"),
            ("scan_ticker", "organizer that can scan ticket")
        ]

class Registration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ticket_uuid = models.UUIDField(
       unique=True,
        editable=False,
        default=uuid.uuid4
    )
    checked_in = models.BooleanField(default=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'event'], name='unique_user_event')]
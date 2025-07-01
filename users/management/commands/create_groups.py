from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from events.models import Events
from users.models import CustomUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        organizer,_ = Group.objects.get_or_create(name='organizers')
        attendee,_ = Group.objects.get_or_create(name='attendee')
        content_type = ContentType.objects.get_for_model(Events)
        permissions = Permission.objects.all()
        organizer.permissions.add(permissions.get(codename='add_events'))
        organizer.permissions.add(permissions.get(codename='view_events'))
        organizer.permissions.add(permissions.get(codename='change_events'))
        organizer.permissions.add(permissions.get(codename='delete_events'))
        organizer.permissions.add(permissions.get(codename='view_own_registration'))
        organizer.permissions.add(permissions.get(codename='view_attendee'))

        attendee.permissions.add(permissions.get(codename='view_events'))
        attendee.permissions.add(permissions.get(codename='can_register'))
        attendee.permissions.add(permissions.get(codename='view_own_registration'))

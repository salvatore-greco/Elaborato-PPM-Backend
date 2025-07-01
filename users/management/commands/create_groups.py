from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from events.models import Events
from users.models import CustomUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        organizer,_ = Group.objects.get_or_create(name='organizers')
        attendee,_ = Group.objects.get_or_create(name='attendee')
        attendee_users = CustomUser.objects.filter(is_organizer=False).only('id')
        organizer_users = CustomUser.objects.filter(is_organizer=True).only('id')
        admin_users = CustomUser.objects.filter(is_superuser=True).only('id')
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

        # Assigning current users a group
        attendee.user_set.add(*attendee_users)
        attendee.user_set.remove(*organizer_users)

        organizer.user_set.add(*organizer_users)
        organizer.user_set.remove(*attendee_users)

        # removing admin from those groups
        attendee.user_set.remove(*admin_users)
        organizer.user_set.remove(*admin_users)

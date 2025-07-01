from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def assign_group_post_registration(sender, instance, created, **kwargs):
    if created:
        if instance.is_organizer:
            group = Group.objects.get(name='organizers')
            print('added user to organizer')
        else:
            group = Group.objects.get(name='attendee')
            print('added user to attendee')
        group.user_set.add(instance.id)

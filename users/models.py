from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_args):
        exception_str = ''
        if not email:
            exception_str+='email '
        if not first_name:
            exception_str+='first name '
        if not last_name:
            exception_str+='last name '
        if exception_str != '':
            raise ValueError(f'The following field are required: {exception_str}')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,**extra_args)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    is_organizer = models.BooleanField(default=False) # Default is attendee
    objects = CustomUserManager()
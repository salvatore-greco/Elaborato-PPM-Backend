from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import CustomUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
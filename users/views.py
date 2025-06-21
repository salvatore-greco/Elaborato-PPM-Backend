from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db import models
from django.shortcuts import render, redirect

from event_management_system.settings import LOGOUT_REDIRECT_URL
from users.forms import LoginForm
from users.models import CustomUser


# Create your views here.
class MyLoginView(LoginView):
    next_page = "home"
    authentication_form = LoginForm

def logout_view(request):
    if CustomUser.is_authenticated:
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)
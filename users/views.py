from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from event_management_system.settings import LOGOUT_REDIRECT_URL
from users.forms import LoginForm, SignUpForm
from users.models import CustomUser


# Create your views here.
class MyLoginView(LoginView):
    next_page = "home"
    authentication_form = LoginForm

def logout_view(request):
    if CustomUser.is_authenticated:
        logout(request)
        return redirect(LOGOUT_REDIRECT_URL)

class RegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

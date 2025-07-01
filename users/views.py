from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from event_management_system.settings import LOGOUT_REDIRECT_URL
from users.forms import LoginForm, SignUpForm
from users.models import CustomUser
from events.models import Events


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


@login_required
def profile_view(request):
    if request.method == 'GET':
        user = request.user
        if user.is_organizer:
            events = Events.objects.filter(organizer_id=user.id)
        else:
            events = Events.objects.filter(registration=user.id)
        return render(request, 'profile.html',
                      {'first_name': user.first_name, 'last_name': user.last_name, 'events': events})

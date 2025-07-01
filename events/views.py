from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import DeletionMixin

from events.forms import EventForm
from events.models import Events

# Create your views here.
# def homepage_view(request):
#     events = Events.objects.all()
#     return render(request, 'home.html', context={'events': events})
class HomepageView(ListView):
    model = Events
    template_name = 'home.html'


def event_details_view(request, id:int) -> HttpResponse :
    user = request.user
    event = get_object_or_404(Events, id=id)
    registered = False
    display_toast = False
    if request.method == 'GET':
        for ev_user in event.registration.all():
            if ev_user.id == user.id:
                registered = True
    else:
        if user.is_authenticated:
            data = int(request.POST.get('btn'))
            display_toast = True
            if data == 1:
                event.registration.add(user)
                registered = True
            elif data == 0:
                event.registration.remove(user)
                registered = False
    return render(request, 'event-details.html', context={'event': event, 'registered': registered, 'toast': display_toast})


class ManageEventView(PermissionRequiredMixin, UpdateView, DeletionMixin):
    form_class = EventForm
    template_name = 'manage.html'
    permission_required = ('events.change_events', 'events.delete_events')
    raise_exception = True
    model = Events

    # Called only by delete from deletion mixin
    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        if form.has_changed():
            messages.add_message(self.request, messages.SUCCESS, 'update')
            return super().form_valid(form)
        return HttpResponseRedirect(self.request.path)

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        if request.user.id != event.organizer_id_id:
            raise PermissionDenied
        data = self.request.POST.get('btn')
        if data == 'update':
            return super().post(request, *args, *kwargs)
        elif data == 'delete':
            messages.add_message(self.request, messages.SUCCESS, 'delete')
            return super().delete(request, *args, *kwargs)
        return None

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        if request.user.id != event.organizer_id_id:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)
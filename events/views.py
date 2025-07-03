from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import F, ExpressionWrapper, BooleanField
from django.db.models.functions import Now
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, TemplateView
from django.views.generic.edit import DeletionMixin
from django.utils.timezone import now
from events.forms import EventForm
from events.models import Events
import json


# Create your views here.
# def homepage_view(request):
#     events = Events.objects.all()
#     return render(request, 'home.html', context={'events': events})
class HomepageView(ListView):
    model = Events
    template_name = 'home.html'
    ordering = 'date'

    def get_queryset(self):
        queryset = super().get_queryset()
        today = now()
        for e in queryset:
            print(f'today {today} e.date {e.date}')
            e.disabled = e.date < today
        return queryset


def event_details_view(request, id: int) -> HttpResponse:
    user = request.user
    event = get_object_or_404(Events, id=id)
    event.disabled = event.date < now()
    registered = False
    display_toast = False
    attendees = None
    attendance = event.registration.count()
    if request.method == 'GET':
        for ev_user in event.registration.all():
            if ev_user.id == user.id:
                registered = True
        if request.user.is_authenticated and request.user.is_organizer and request.user.id == event.organizer_id_id:
            attendees = event.registration.all()
    else:
        if user.is_authenticated and not event.disabled:
            data = int(request.POST.get('btn'))
            display_toast = True
            if data == 1:
                event.registration.add(user)
                registered = True
            elif data == 0:
                event.registration.remove(user)
                registered = False
    context = {
        'event': event,
        'registered': registered,
        'toast': display_toast,
        'attendance': attendance,
        'attendees': attendees
    }
    return render(request, 'event-details.html', context=context)


class ManageEventView(PermissionRequiredMixin, UpdateView, DeletionMixin):
    form_class = EventForm
    template_name = 'manage.html'
    permission_required = ('events.change_events', 'events.delete_events')
    raise_exception = True
    model = Events
    extra_context = {'disabled': None}

    # Called only by delete from deletion mixin
    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        if form.has_changed():
            messages.add_message(self.request, messages.SUCCESS, 'update')
            super().form_valid(form)
        return HttpResponseRedirect(self.request.path)

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        if request.user.id != event.organizer_id_id:
            raise PermissionDenied
        data = self.request.POST.get('btn')
        if data == 'update' and not self.extra_context['disabled']:
            return super().post(request, *args, *kwargs)
        elif data == 'delete' and not self.extra_context['disabled']:
            messages.add_message(self.request, messages.SUCCESS, 'delete')
            return super().delete(request, *args, *kwargs)
        return None

    def get(self, request, *args, **kwargs):
        event = self.get_object()
        self.extra_context['disabled'] = event.date < now()
        if request.user.id != event.organizer_id_id:
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


class CreateEventView(PermissionRequiredMixin, CreateView):
    model = Events
    form_class = EventForm
    template_name = 'event-create.html'
    permission_required = 'events.add_events'
    raise_exception = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.organizer_id_id = self.request.user.id
        messages.add_message(self.request, messages.SUCCESS, 'created')
        return super().form_valid(form)


class CheckInView(TemplateView):
    template_name = 'check-in.html'


def validate_ticket(request):
    if request.method == 'POST':
        request.session['data'] = json.loads(request.body)
        return redirect(reverse('events:validation-success'))
    return HttpResponseNotAllowed(permitted_methods='POST')

def validation_success(request):
    if request.method == 'GET':
        return render(request, 'validation_result.html', context={'data':request.session['data']})
    return HttpResponseNotAllowed(permitted_methods='GET')

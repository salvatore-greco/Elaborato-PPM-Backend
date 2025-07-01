from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from events.models import Events
# Create your views here.
# def homepage_view(request):
#     events = Events.objects.all()
#     return render(request, 'home.html', context={'events': events})
class HomepageView(ListView):
    model = Events
    template_name = 'home.html'


def event_details_view(request, id):
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
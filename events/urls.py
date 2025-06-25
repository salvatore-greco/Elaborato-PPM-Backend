from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path("<int:id>", views.event_details_view, name='event-details')
]

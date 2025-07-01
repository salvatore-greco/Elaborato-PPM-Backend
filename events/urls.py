from django.urls import path
from . import views
from .views import ManageEventView

app_name = 'events'

urlpatterns = [
    path("<int:id>", views.event_details_view, name='event-details'),
    path("<pk>/manage", ManageEventView.as_view(), name='organizer-manage')
]

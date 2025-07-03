from django.urls import path
from . import views
from .views import ManageEventView, CreateEventView, CheckInView

app_name = 'events'

urlpatterns = [
    path("<int:id>", views.event_details_view, name='event-details'),
    path("<pk>/manage", ManageEventView.as_view(), name='organizer-manage'),
    path("create", CreateEventView.as_view(), name="organizer-create"),
    path("checkin", CheckInView.as_view(), name="checkin"),
    path('validate', views.validate_ticket, name='validate'),
    path('validation-success', views.validation_success, name='validation-success')
]

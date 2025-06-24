from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.RegistrationView.as_view(), name="register"),
]
# greeter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Maps the root URL of the app ('') to the greet_user view
    path('', views.greet_user, name='greet_user'),
]
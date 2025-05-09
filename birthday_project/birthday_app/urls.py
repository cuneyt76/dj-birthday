from django.urls import path
from . import views

app_name = 'birthday_app'

urlpatterns = [
    path('', views.birthday_form_view, name='birthday_form'),
]
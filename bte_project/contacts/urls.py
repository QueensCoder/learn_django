from django.urls import path
from . import views
urlpatterns = [
    path('contact', views.contact, name='contact')
]

# urls is linked to views.py

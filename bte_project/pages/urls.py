from django.urls import path
from . import views

# matches url patterns
# uses views to render html based on view methods
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

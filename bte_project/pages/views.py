from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# some sort of render/ routing displays html
# upon request


def index(req):
    return render(req, 'pages/index.html')


def about(req):
    return render(req, 'pages/about.html')

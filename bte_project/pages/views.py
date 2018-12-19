from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# some sort of render/ routing displays html
# upon request

from listings.models import Listing
from realtors.models import Realtor


def index(req):
    listings = Listing.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(req, 'pages/index.html', context)


def about(req):
    # get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(req, 'pages/about.html', context)

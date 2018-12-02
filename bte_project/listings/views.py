from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, 'listings/listings.html')

# takes request and sends it to html


def listing(req):
    return render(req, 'listings/listing.html')


def search(req):
    return render(req, 'listings/search.html')


# need to return the render method with the request and
# html to diplay

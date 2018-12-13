from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def index(req):
    listings = Listing.objects.order_by('-list_date').filter(is_published=true)
 # .all() to get all can use order by list date earliest first
 # filter allows us to show only published listings
    paginator = Paginator(listings, 2)
    page = req.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(req, 'listings/listings.html', context)

# takes request and sends it to html


def listing(req, listing_id):
    return render(req, 'listings/listing.html')


def search(req):
    return render(req, 'listings/search.html')


# need to return the render method with the request and
# html to diplay

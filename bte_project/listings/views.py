from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


# Create your views here.


def index(req):
    listings = Listing.objects.order_by('-list_date').filter(is_published=true)
 # .all() to get all can use order by list date earliest first
 # filter allows us to show only published listings
    paginator = Paginator(listings, 2)
    page = req.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
    }
    return render(req, 'listings/listings.html', context)

# takes request and sends it to html

# get one  listing by id
# if  id not found return 404


def listing(req, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(req, 'listings/listing.html', context)


def search(req):

    queryset_list = Listing.objects.order_by('-list_date')

    # key words

   # if key words are in GET req use those key words
   # to filter the queryset from the data base
   # see description__
    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        queryset_list = queryset_list.filter(description__icontains=keywords)

# city
    if 'city' in req.GET:
        city = req.GET['city']
        # iexact is case insensitive
        queryset_list = queryset_list.filter(city__iexact=city)

# state
    if 'state' in req.GET:
        state = req.GET['state']
        # iexact is case insensitive
        queryset_list = queryset_list.filter(state__iexact=state)

# bedrooms
    if 'bedrooms' in req.GET:
        bedrooms = req.GET['bedrooms']
        # iexact is case insensitive
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)


# context for what is passed to html
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': req.GET
    }

    return render(req, 'listings/search.html', context)


# need to return the render method with the request and
# html to diplay

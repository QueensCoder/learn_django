from django.contrib import admin
from .models import Listing

# Register your models here.

# before registering model ...add these fields to display in admin view


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    # make the fields a link to the data entry in admin area

    # adds filter functionality to admin dashboard
    # can filter by realtor now
    list_filter = ('realtor',)

    list_editable = ('is_published',)
    # edit from admin view
    # use comma after if one item is passed in

    search_fields = ('title', 'description',
                     'city', 'zipcode', 'price')
    # search functionality


# register listing or other admin items
admin.site.register(Listing, ListingAdmin)
# fields in listing will reflect the model

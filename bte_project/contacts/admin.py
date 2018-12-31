from django.contrib import admin

# Register your models here.

from .models import Contact

# how to register a model to the admin area


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
# list display gives names to fields pulled from db
# links are what is a link in admin area
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

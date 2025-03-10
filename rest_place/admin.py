from django.contrib import admin
from .models import Country, Region, RestPlace, Favourite

# admin.site.register(Country)
# admin.site.register(Region)
admin.site.register(RestPlace)
admin.site.register(Favourite)

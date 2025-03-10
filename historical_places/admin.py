from django.contrib import admin
from .models import Country, Region, HistoricalPlace, Favourite

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(HistoricalPlace)
admin.site.register(Favourite)

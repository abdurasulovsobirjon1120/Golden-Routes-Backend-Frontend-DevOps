from django.urls import path
from apps.historical_places.api_endpoints import CountryListView, RegionDetailView

urlpatterns = [
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("places/region/<int:pk>/", RegionDetailView.as_view(), name="region-detail")
]

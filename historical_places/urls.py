from django.urls import path
from .views import (
    CountryListCreateView, RegionListView, RegionDetailView, HistoricalPlaceListCreateView,
    HistoricalPlaceDetailView, FavouriteView, RateHistoricalPlace, CommentHistoricalPlace
)

urlpatterns = [
    # Countries API
    path('countries/', CountryListCreateView.as_view(), name='country-list'),

    # Regions API
    path('places/region/', RegionListView.as_view(), name='region-list'),
    path('places/region/<int:pk>/', RegionDetailView.as_view(), name='region-detail'),

    # Historical Places API
    path('places/', HistoricalPlaceListCreateView.as_view(), name='historical-place-list'),
    path('places/<int:pk>/', HistoricalPlaceDetailView.as_view(), name='historical-place-detail'),

    # Favourite API
    path('places/<int:place_id>/favourite/', FavouriteView.as_view(), name='historical-place-favourite'),

    # Rating API (Stars)
    path('places/<int:place_id>/rate/', RateHistoricalPlace.as_view(), name='historical-place-rate'),

    # Comments API
    path('places/<int:place_id>/comment/', CommentHistoricalPlace.as_view(), name='historical-place-comment'),
]

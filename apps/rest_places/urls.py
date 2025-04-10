from django.urls import path
from apps.rest_places.api_endpoints import (
    CountryListCreateView, RestPlaceListCreateView,
    RestPlaceDetailView, FavouriteView, RateRestPlace, CommentRestPlace
)

urlpatterns = [
    # Countries API
    path('countries/', CountryListCreateView.as_view(), name='country-list'),

    # Rest Places API
    path('rest_places/', RestPlaceListCreateView.as_view(), name='restplace-list'),
    path('rest_places/<int:pk>/', RestPlaceDetailView.as_view(), name='restplace-detail'),

    # Favourite API
    path('rest_places/<int:place_id>/favourite/', FavouriteView.as_view(), name='restplace-favourite'),

    # Rating API (Stars)
    path('rest_places/<int:place_id>/rate/', RateRestPlace.as_view(), name='restplace-rate'),

    # Comments API
    path('rest_places/<int:place_id>/comment/', CommentRestPlace.as_view(), name='restplace-comment'),
]
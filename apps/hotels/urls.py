from django.urls import path
from apps.hotels.api_endpoints import (
    HotelCreateView, HotelEditView, HotelListView,
    CommentCreateView, CommentListView, CommentDeleteView,
    AddFavouriteView, RemoveFavouriteView
)

urlpatterns = [
    path('add/', HotelCreateView.as_view(), name='hotel-add'),
    path('edit/<int:pk>/', HotelEditView.as_view(), name='hotel-edit'),
    path('list/', HotelListView.as_view(), name='hotel-list'),
    path('regions/', HotelListView.as_view(), name='region-list'),
    # path('regions/<int:region_id>/hotel/', RegionHotelListView.as_view(), name='region-hotel-list'),
    path('comment/add/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('favourite/add/', AddFavouriteView.as_view(), name='favourite-add'),
    path('favourite/delete/<int:pk>/', RemoveFavouriteView.as_view(), name='favourite-delete'),
#     path('hotels/rate/add/', RatingAddView.as_view(), name='rating-add'),
#     path('restaurants/rate/', RatingListView.as_view(), name='rating-list'),
]

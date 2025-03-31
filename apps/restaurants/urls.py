from django.urls import path
from apps.restaurants import api_endpoints 

urlpatterns = [
    path('restaurants/add/', api_endpoints.RestaurantCreateAPIView.as_view(), name='restaurant-add'),
    path('restaurants/edit/<int:id>/', api_endpoints.RestaurantUpdateAPIView.as_view(), name='restaurant-edit'),

    path('regions/', api_endpoints.RegionListView.as_view(), name='region-list'),
    path('regions/restaurant/', api_endpoints.AllRestaurantsListView.as_view(), name='all-restaurants'),
    path('regions/<int:region_id>/restaurant/', api_endpoints.RegionRestaurantsListView.as_view(), name='region-restaurants'),

    path('restaurants/comment/', api_endpoints.CommentListView.as_view(), name='comment-list'),
    path('restaurants/comment/add/', api_endpoints.CommentCreateView.as_view(), name='comment-add'),
    path('restaurants/comment/delete/<int:id>/', api_endpoints.CommentDeleteView.as_view(), name='comment-delete'),

    path('restaurants/favourite/add/<int:id>/', api_endpoints.AddFavouriteView.as_view(), name='add-favourite'),
    path('restaurants/favourite/delete/<int:id>/', api_endpoints.RemoveFavouriteView.as_view(), name='remove-favourite'),
    path('restaurants/favourite/', api_endpoints.UserFavouritesView.as_view(), name='user-favourites'),

]
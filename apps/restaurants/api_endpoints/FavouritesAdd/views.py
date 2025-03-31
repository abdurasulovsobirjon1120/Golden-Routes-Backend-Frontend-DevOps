from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from apps.restaurants.models import Restaurant
from .serializers import FavouriteRestaurantSerializer

class AddFavouriteView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = FavouriteRestaurantSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        restaurant = self.get_object()
        user = request.user
        
        if user in restaurant.favourites.all():
            return Response(
                {'success': False, 'message': 'Restaurant already in favorites'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        restaurant.favourites.add(user)
        return Response(
            {
                'success': True,
                'message': 'Restaurant added to favorites',
                'data': self.get_serializer(restaurant).data
            },
            status=status.HTTP_200_OK
        )

class UserFavouritesView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavouriteRestaurantSerializer

    def get_queryset(self):
        return self.request.user.favourite_restaurants.all()
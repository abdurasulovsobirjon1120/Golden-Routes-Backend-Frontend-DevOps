from rest_framework import generics, permissions, status
from rest_framework.response import Response
from apps.hotels.models import Hotel
from .serializers import FavouriteHotelSerializer

class AddFavouriteView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hotel.objects.all()
    serializer_class = FavouriteHotelSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        restaurant = self.get_object()
        user = request.user
        
        if user in restaurant.favourites.all():
            return Response(
                {'success': False, 'message': 'Hotel already in favorites'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        restaurant.favourites.add(user)
        return Response(
            {
                'success': True,
                'message': 'Hotel added to favorites',
                'data': self.get_serializer(restaurant).data
            },
            status=status.HTTP_200_OK
        )

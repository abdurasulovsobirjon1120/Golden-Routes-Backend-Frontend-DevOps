from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.historical_places.models import Region  
from apps.restaurants.models import Restaurant
from .serializers import (
    RestaurantDetailSerializer
)

class RegionRestaurantsListView(generics.ListAPIView):
    serializer_class = RestaurantDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return Restaurant.objects.filter(
            region_id=region_id
        ).select_related('region').order_by('-stars')
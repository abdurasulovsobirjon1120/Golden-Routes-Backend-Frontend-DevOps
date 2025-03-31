from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.historical_places.models import Region  
from apps.restaurants.models import Restaurant
from .serializers import (
    RegionSerializer
)

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [AllowAny]
    pagination_class = None
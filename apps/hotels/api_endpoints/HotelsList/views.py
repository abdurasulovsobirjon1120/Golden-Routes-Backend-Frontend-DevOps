from rest_framework import generics
from apps.hotels.models import Hotel
from .serializers import HotelListSerializer

class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
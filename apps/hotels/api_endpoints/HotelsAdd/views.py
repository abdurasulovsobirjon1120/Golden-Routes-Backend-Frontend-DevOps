from rest_framework import generics, permissions
from apps.hotels.models import Hotel
from .serializers import HotelAddSerializer


class HotelCreateView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelAddSerializer
    permission_classes = [permissions.IsAuthenticated]

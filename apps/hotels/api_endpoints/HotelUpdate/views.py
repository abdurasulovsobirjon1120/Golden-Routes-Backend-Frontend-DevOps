from rest_framework import generics, permissions
from apps.hotels.models import Hotel
from .serializers import HotelEditSerializer

class HotelEditView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelEditSerializer
    permission_classes = [permissions.IsAuthenticated]
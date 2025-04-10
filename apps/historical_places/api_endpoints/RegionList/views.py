from rest_framework import generics
from rest_framework import permissions
from apps.historical_places.models import Region
from .serializers import RegionListSerializer

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer  
    permission_classes = [permissions.AllowAny]

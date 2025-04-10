from rest_framework import generics
from rest_framework import permissions
from apps.historical_places.models import Region
from .serializers import RegionDetailSerializer

class RegionDetailView(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer 
    permission_classes = [permissions.AllowAny]
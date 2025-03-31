from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from apps.historical_places.models import Region
from .serializers import RegionDetailSerializer

class RegionDetailView(RetrieveAPIView):
    queryset = Region.objects.prefetch_related("historical_places").all()
    serializer_class = RegionDetailSerializer
    permission_classes = [permissions.AllowAny]

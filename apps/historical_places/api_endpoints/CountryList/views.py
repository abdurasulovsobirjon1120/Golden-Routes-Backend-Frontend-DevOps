from rest_framework.generics import ListAPIView
from rest_framework import permissions
from apps.historical_places.models import Country
from .serializers import CountrySerializer

class CountryListView(ListAPIView):
    queryset = Country.objects.prefetch_related("regions").all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]

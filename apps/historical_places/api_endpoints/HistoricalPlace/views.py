from apps.historical_places.models import HistoricalPlace
from .serializers import HistoricalPlaceSerializer
from rest_framework import permissions
from rest_framework import generics


class HistoricalPlaceListCreateView(generics.ListCreateAPIView):
    queryset = HistoricalPlace.objects.all()
    serializer_class = HistoricalPlaceSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class HistoricalPlaceDetailView(generics.RetrieveAPIView):
    queryset = HistoricalPlace.objects.all()
    serializer_class = HistoricalPlaceSerializer
    permission_classes = [permissions.AllowAny]
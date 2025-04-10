from apps.rest_places.models import RestPlace
from .serializers import RestPlaceSerializer
from rest_framework import permissions
from rest_framework import generics


class RestPlaceListCreateView(generics.ListCreateAPIView):
    queryset = RestPlace.objects.all()
    serializer_class = RestPlaceSerializer

    def get_permissions(self):
        """GET so‘rovlari hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class RestPlaceDetailView(generics.RetrieveAPIView):
    queryset = RestPlace.objects.all()
    serializer_class = RestPlaceSerializer
    permission_classes = [permissions.AllowAny] 
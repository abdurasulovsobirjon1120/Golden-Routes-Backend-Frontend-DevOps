from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from apps.historical_places.models import Country
from .serializers import CountrySerializer
from rest_framework import permissions
from rest_framework import generics


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        """GET hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.restaurants.models import Restaurant
from .serializers import (
    RestaurantListSerializer
)

class AllRestaurantsListView(generics.ListAPIView):
    queryset = Restaurant.objects.select_related('region').all()
    serializer_class = RestaurantListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return super().get_queryset().order_by('-stars')
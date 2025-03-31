from rest_framework import serializers
from apps.restaurants.models import Restaurant
from apps.restaurants.api_endpoints.RegionList import RegionSerializer


class RestaurantDetailSerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)
    
    class Meta:
        model = Restaurant
        fields = '__all__'
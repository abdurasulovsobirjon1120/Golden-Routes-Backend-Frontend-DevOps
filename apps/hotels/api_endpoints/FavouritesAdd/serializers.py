from rest_framework import serializers
from apps.hotels.models import Hotel

class FavouriteHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'image', 'stars']

from rest_framework import serializers
from apps.hotels.models import Hotel

class HotelEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
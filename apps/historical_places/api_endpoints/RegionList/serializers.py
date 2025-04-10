from rest_framework import serializers
from apps.historical_places.models import  Region

class RegionListSerializer(serializers.ModelSerializer):
    """Faqatgina region ma'lumotlarini qaytaradigan serializer"""
    class Meta:
        model = Region
        fields = ["id", "region", "country"] 
from rest_framework import serializers
from .models import Country, Region, HistoricalPlace, Favourite

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class RegionListSerializer(serializers.ModelSerializer):
    """Faqatgina region ma'lumotlarini qaytaradigan serializer"""
    class Meta:
        model = Region
        fields = ["id", "region", "country"]  # historical_places kiritilmagan

class HistoricalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPlace
        fields = "__all__"

class RegionDetailSerializer(serializers.ModelSerializer):
    """Bitta region va unga tegishli historical places ma'lumotlarini qaytaradi"""
    historical_places = HistoricalPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ["id", "region", "country", "historical_places"]


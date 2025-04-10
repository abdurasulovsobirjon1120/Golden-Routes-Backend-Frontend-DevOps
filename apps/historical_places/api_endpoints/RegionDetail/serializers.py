from rest_framework import serializers
from apps.historical_places.models import  Region, HistoricalPlace


class HistoricalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPlace
        fields = "__all__"
        ref_name = 'HistoricalPlaceSerializer_RegionDetail'

class RegionDetailSerializer(serializers.ModelSerializer):
    """Bitta region va unga tegishli historical places ma'lumotlarini qaytaradi"""
    historical_places = HistoricalPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ["id", "region", "country", "historical_places"]
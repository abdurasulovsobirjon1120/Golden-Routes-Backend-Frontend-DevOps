from rest_framework import serializers
from apps.historical_places.models import Region, HistoricalPlace

class HistoricalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPlace
        fields = [
            "id", "name", "description", "location", "entry_price", 
            "image", "stars", "total_reviews", "comments"
        ]

class RegionDetailSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(source="country.id", read_only=True)
    historical_places = HistoricalPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ["id", "region", "country", "historical_places"]

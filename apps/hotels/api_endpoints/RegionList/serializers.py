from rest_framework import serializers
from apps.historical_places.models import Region, Country 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country']
        ref_name = 'HistoricalPlacesCountrySerializer'

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    
    class Meta:
        model = Region
        fields = ['id', 'region', 'country', 'created_at']
        ref_name = 'HistoricalPlacesRegionSerializer' 

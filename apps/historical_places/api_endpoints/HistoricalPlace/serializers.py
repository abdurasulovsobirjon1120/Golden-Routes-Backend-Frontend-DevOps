from rest_framework import serializers
from apps.historical_places.models import HistoricalPlace


class HistoricalPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPlace
        fields = "__all__"
        ref_name = 'HistoricalPlaceSerializer_Main'
from rest_framework import serializers
from apps.rest_places.models import RestFavourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestFavourite
        fields = '__all__'
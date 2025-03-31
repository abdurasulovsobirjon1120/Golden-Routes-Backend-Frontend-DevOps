from rest_framework import serializers
from apps.restaurants.models import Restaurant

class FavouriteRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'image', 'stars']

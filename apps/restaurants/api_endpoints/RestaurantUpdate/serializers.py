from rest_framework import serializers
from apps.restaurants.models import Restaurant

class RestaurantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'working_time', 'phone_number',
            'description', 'location', 'image', 'stars',
            'comment', 'favourite'
        ]
        extra_kwargs = {
            'name': {'required': False},
            'phone_number': {'required': False},
            'image': {'required': False}
        }

    def validate_phone_number(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("Telefon raqam faqat raqamlardan iborat bo'lishi kerak")
        return value

    def validate(self, data):
        if not any(data.values()):
            raise serializers.ValidationError("Hech bo'lmaganda bitta maydon yangilanishi kerak")
        return data
from rest_framework import serializers
from apps.restaurants.models import Restaurant

class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'working_time', 'phone_number', 
            'description', 'location', 'image', 'stars'
        ]
        extra_kwargs = {
            'name': {
                'required': True,
                'error_messages': {
                    'required': "Restoran nomi kiritilishi shart",
                    'blank': "Restoran nomi bo'sh bo'lishi mumkin emas"
                }
            },
            'phone_number': {
                'required': True,
                'error_messages': {
                    'required': "Telefon raqami kiritilishi shart",
                    'blank': "Telefon raqami bo'sh bo'lishi mumkin emas"
                }
            },
            'image': {'required': False}
        }

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Telefon raqam faqat raqamlardan iborat bo'lishi kerak")
        if len(value) < 9:
            raise serializers.ValidationError("Telefon raqam juda qisqa")
        return value

    def validate_stars(self, value):
        if value is not None and (value < 0 or value > 5):
            raise serializers.ValidationError("Yulduzlar 0 dan 5 gacha bo'lishi kerak")
        return value
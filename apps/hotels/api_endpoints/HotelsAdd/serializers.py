from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.hotels.models import Hotel

class HotelAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate_name(self, value):
        if Hotel.objects.filter(name=value).exists():
            raise ValidationError("Hotel nomi allaqachon mavjud.")
        return value
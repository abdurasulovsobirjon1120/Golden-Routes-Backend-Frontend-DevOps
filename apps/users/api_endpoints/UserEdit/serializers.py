from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["full_name", "username", "profile_photo", "phone_number", "gender", "age"]
        extra_kwargs = {
            "username": {"required": False, "allow_blank": True},
            "profile_photo": {"required": False},
            "phone_number": {"required": False},
            "gender": {"required": False},
            "age": {"required": False}
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
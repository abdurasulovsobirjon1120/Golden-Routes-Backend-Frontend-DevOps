from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(max_length=6, required=True)

    def validate(self, data):
        email = data.get("email")
        code = data.get("code")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        if user.verification_code != code:
            raise serializers.ValidationError("Invalid verification code.")

        data["user"] = user 
        return data

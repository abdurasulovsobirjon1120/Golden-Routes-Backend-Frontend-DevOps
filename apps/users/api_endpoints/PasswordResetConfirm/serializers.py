from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": _("User not found")})

        if user.reset_password_code != data["code"]:
            raise serializers.ValidationError({"code": _("Invalid reset code")})

        user.set_password(data["new_password"])
        user.reset_password_code = None
        user.save()
        return data
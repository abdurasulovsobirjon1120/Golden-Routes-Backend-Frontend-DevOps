from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from apps.users.utils import generate_code, send_reset_password_email
from django.contrib.auth import get_user_model

User = get_user_model()

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": _("User not found")})

        reset_code = generate_code()
        user.reset_password_code = reset_code
        user.save()

        send_reset_password_email(user.email, reset_code)
        return data
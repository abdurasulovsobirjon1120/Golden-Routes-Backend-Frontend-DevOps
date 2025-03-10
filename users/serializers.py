from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User
from .utils import generate_code, send_verification_email, send_reset_password_email


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "password", "confirm_password", "phone_number", "gender", "age", "username", "profile_photo"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"password": _("Passwords do not match!")})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")  # Parolni tasdiqlashni o‘chiramiz

        email = validated_data["email"]
        full_name = validated_data["full_name"]
        phone_number = validated_data.get("phone_number", None)
        password = validated_data["password"]
        gender = validated_data.get("gender", None)
        age = validated_data.get("age", 18)
        username = validated_data.get("username", None)
        profile_photo = validated_data.get("profile_photo", None)

        # Foydalanuvchi yaratish (lekin email tasdiqlanmagan holatda)
        user = User.objects.create_user(
            email=email, full_name=full_name, password=password, phone_number=phone_number,
            gender=gender, age=age, username=username, profile_photo=profile_photo
        )

        # Email uchun tasdiqlash kodi generatsiya qilish
        verification_code = generate_code()
        user.email_verification_code = verification_code
        user.save()

        # Tasdiqlash kodini emailga yuborish
        send_verification_email(user.email, verification_code)

        return user


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": _("User not found")})

        if user.email_verification_code != data["code"]:
            raise serializers.ValidationError({"code": _("Invalid verification code")})

        # Email tasdiqlandi
        user.email_verification_code = None
        user.save()
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": _("User not found")})

        # Parolni tiklash uchun kod generatsiya qilish
        reset_code = generate_code()
        user.reset_password_code = reset_code
        user.save()

        # Kodni emailga yuborish
        send_reset_password_email(user.email, reset_code)
        return data


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

        # Yangi parolni saqlash
        user.set_password(data["new_password"])
        user.reset_password_code = None
        user.save()
        return data


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

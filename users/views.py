from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import (
    RegisterSerializer, VerifyEmailSerializer, LoginSerializer,
    ResetPasswordRequestSerializer, ResetPasswordSerializer, UserUpdateSerializer
)
from .utils import generate_code, send_verification_email, send_reset_password_email


def get_tokens_for_user(user):
    """Foydalanuvchi uchun access va refresh token yaratadi"""
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        tokens = get_tokens_for_user(user)

        return Response(
            {
                "message": "Verification code sent to email",
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED
        )


class VerifyEmailView(generics.GenericAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=request.data["email"])
        user.is_active = True  # Email tasdiqlanganda akkaunt faollashtiriladi
        user.email_verification_code = None
        user.save()

        tokens = get_tokens_for_user(user)

        return Response(
            {"message": "Email verified successfully", "tokens": tokens},
            status=status.HTTP_200_OK
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(email=serializer.validated_data["email"], password=serializer.validated_data["password"])

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        if not user.is_active:
            return Response({"error": "Account is not verified"}, status=status.HTTP_400_BAD_REQUEST)

        tokens = get_tokens_for_user(user)

        return Response(
            {
                "message": "Login successful",
            },
            status=status.HTTP_200_OK
        )



class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh", None)

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordRequestView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"message": "Reset code sent to email"}, status=status.HTTP_200_OK)


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=request.data["email"])
        user.set_password(request.data["new_password"])
        user.reset_password_code = None  # Reset kod o‘chiriladi
        user.save()

        tokens = get_tokens_for_user(user)

        return Response(
            {"message": "Password reset successfully", "tokens": tokens},
            status=status.HTTP_200_OK
        )


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Foydalanuvchi faqat o‘z profilini tahrirlay oladi

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        user = self.get_object()

        tokens = get_tokens_for_user(user)

        response.data["tokens"] = tokens
        return response

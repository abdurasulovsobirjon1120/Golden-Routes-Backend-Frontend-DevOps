from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import LoginSerializer
from apps.users.models import User
from apps.users.utils import generate_code
import logging

logger = logging.getLogger(__name__)  # Logger yaratish


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")  # ✅ Use email instead of phone_number
            password = serializer.validated_data.get("password")

            try:
                user = User.objects.get(email=email)  # ✅ Get user by email

                if user.check_password(password):
                    code = generate_code()
                    user.verification_code = code  # ✅ Kodni foydalanuvchi modeliga saqlash
                    user.save()

                    # ✅ Kodni terminalga chiqarish (log fayliga ham yoziladi)
                    logger.info(f"Verification code for {email}: {code}")
                    print(f"Verification code for {email}: {code}")

                    # ✅ Generate authentication token (assuming you're using Simple JWT)
                    from rest_framework_simplejwt.tokens import RefreshToken
                    refresh = RefreshToken.for_user(user)

                    return Response({
                        "message": "Login successful",
                        "refresh_token": str(refresh),
                        "access_token": str(refresh.access_token),
                    }, status=status.HTTP_200_OK)
                
                else:
                    return Response({
                        "error": "Invalid login credentials"
                    }, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({
                    "error": "User not found"
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

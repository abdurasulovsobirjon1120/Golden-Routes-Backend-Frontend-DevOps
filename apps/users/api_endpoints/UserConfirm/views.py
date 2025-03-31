from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .serializers import VerifyEmailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class VerifyEmailView(GenericAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = (permissions.AllowAny,)

    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]

            user.is_verified = True
            user.verification_code = None 
            user.save()

            return Response(
                {"message": "Email verified successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

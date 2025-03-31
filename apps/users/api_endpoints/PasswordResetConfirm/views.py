from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import ResetPasswordSerializer


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
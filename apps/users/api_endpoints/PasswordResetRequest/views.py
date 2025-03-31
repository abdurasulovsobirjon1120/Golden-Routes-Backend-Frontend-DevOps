from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializers import ResetPasswordRequestSerializer

class ResetPasswordRequestView(generics.GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"message": "Reset code sent to email"}, status=status.HTTP_200_OK)

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from apps.restaurants.models import Comment
from .serializers import CommentCreateSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'success': True,
                'message': 'Comment successfully added',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
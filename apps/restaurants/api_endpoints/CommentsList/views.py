from rest_framework import generics, permissions
from apps.restaurants.models import Comment
from .serializers import (
    CommentSerializer
)

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Comment.objects.select_related('user', 'restaurant').order_by('-created_at')

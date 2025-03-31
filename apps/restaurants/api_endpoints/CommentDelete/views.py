from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from apps.restaurants.models import Comment



class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response(
                {'success': False, 'message': 'You can only delete your own comments'},
                status=status.HTTP_403_FORBIDDEN
            )
        self.perform_destroy(instance)
        return Response(
            {'success': True, 'message': 'Comment successfully deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
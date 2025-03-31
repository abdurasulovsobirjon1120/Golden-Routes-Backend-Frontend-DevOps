from rest_framework import serializers
from apps.restaurants.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['hotel', 'text']
        extra_kwargs = {
            'hotel': {'required': True},
            'text': {'required': True, 'min_length': 10}
        }
        ref_name = "HotelCommentAdd"
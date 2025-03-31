from rest_framework import serializers
from apps.restaurants.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['restaurant', 'text']
        extra_kwargs = {
            'restaurant': {'required': True},
            'text': {'required': True, 'min_length': 10}
        }
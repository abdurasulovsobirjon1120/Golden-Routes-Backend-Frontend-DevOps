from apps.historical_places.models import HistoricalPlace
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class CommentHistoricalPlace(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, place_id):
        place = get_object_or_404(HistoricalPlace, id=place_id)
        comment_text = request.data.get("comment", "").strip()

        if not comment_text:
            return Response({"error": "Comment cannot be empty."}, status=400)

        place.comment = f"{place.comment}\n{comment_text}" if place.comment else comment_text
        place.save()

        return Response({"message": "Comment added!"}, status=201)
from apps.rest_places.models import RestPlace
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class RateRestPlace(APIView):
    permission_classes = [permissions.AllowAny]  # Hamma baho bera oladi

    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        rating = request.data.get("stars", 0)

        if not (0 <= float(rating) <= 5):
            return Response({"error": "Invalid rating. Must be between 0 and 5."}, status=400)

        place.update_stars(float(rating))
        return Response({"message": "Rating updated!"})


class CommentRestPlace(APIView):
    permission_classes = [permissions.AllowAny]  
    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        comment_text = request.data.get("comment", "").strip()

        if not comment_text:
            return Response({"error": "Comment cannot be empty."}, status=400)

        place.comments = f"{place.comments}\n{comment_text}" if place.comments else comment_text
        place.save()

        return Response({"message": "Comment added!"}, status=201)
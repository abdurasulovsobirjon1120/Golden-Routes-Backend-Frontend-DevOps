from apps.historical_places.models import HistoricalPlace
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class RateHistoricalPlace(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, place_id):
        place = get_object_or_404(HistoricalPlace, id=place_id)
        rating = request.data.get("stars", 0)

        try:
            rating = float(rating)
        except ValueError:
            return Response({"error": "Invalid rating format. Must be a number."}, status=400)

        if not (0 <= rating <= 5):
            return Response({"error": "Invalid rating. Must be between 0 and 5."}, status=400)

        place.update_stars(rating)
        return Response({"message": "Rating updated!"})
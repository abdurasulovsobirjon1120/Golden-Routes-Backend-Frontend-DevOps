from apps.historical_places.models import HistoricalFavourite, HistoricalPlace
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class FavouriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, place_id):
        place = get_object_or_404(HistoricalPlace, id=place_id)
        fav, created = HistoricalFavourite.objects.get_or_create(user=request.user, place=place)
        return Response({"message": "Added to favourites!"} if created else {"message": "Already in favourites!"})

    def delete(self, request, place_id):
        fav = HistoricalFavourite.objects.filter(user=request.user, place_id=place_id)
        if fav.exists():
            fav.delete()
            return Response({"message": "Removed from favourites!"})
        return Response({"error": "Not found in favourites!"}, status=400)

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from apps.rest_places.models import RestPlace, RestFavourite

class FavouriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        fav, created = RestFavourite.objects.get_or_create(user=request.user, place=place)
        return Response({"message": "Added to favourites!"} if created else {"message": "Already in favourites!"})

    def delete(self, request, place_id):
        fav = RestFavourite.objects.filter(user=request.user, place_id=place_id)
        if fav.exists():
            fav.delete()
            return Response({"message": "Removed from favourites!"})
        return Response({"error": "Not found in favourites!"}, status=400)

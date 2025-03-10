from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Country, Region, RestPlace, Favourite
from .serializers import CountrySerializer, RegionSerializer, RestPlaceSerializer, FavouriteSerializer
from rest_framework.permissions import AllowAny


# Country API
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        """GET so‘rovlari hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [AllowAny()]


# Region API
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_permissions(self):
        """GET so‘rovlari hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [AllowAny()]


# Rest Places API
class RestPlaceListCreateView(generics.ListCreateAPIView):
    queryset = RestPlace.objects.all()
    serializer_class = RestPlaceSerializer

    def get_permissions(self):
        """GET so‘rovlari hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [AllowAny()]


class RestPlaceDetailView(generics.RetrieveAPIView):
    queryset = RestPlace.objects.all()
    serializer_class = RestPlaceSerializer
    permission_classes = [AllowAny]  # Foydalanuvchilar bitta joyni ko'rishi mumkin


# Favourite API
class FavouriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        fav, created = Favourite.objects.get_or_create(user=request.user, place=place)
        return Response({"message": "Added to favourites!"} if created else {"message": "Already in favourites!"})

    def delete(self, request, place_id):
        fav = Favourite.objects.filter(user=request.user, place_id=place_id)
        if fav.exists():
            fav.delete()
            return Response({"message": "Removed from favourites!"})
        return Response({"error": "Not found in favourites!"}, status=400)


# Rating (Stars) API
class RateRestPlace(APIView):
    permission_classes = [AllowAny]  # Hamma baho bera oladi

    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        rating = request.data.get("stars", 0)

        if not (0 <= float(rating) <= 5):
            return Response({"error": "Invalid rating. Must be between 0 and 5."}, status=400)

        place.update_stars(float(rating))
        return Response({"message": "Rating updated!"})


# Comment API
class CommentRestPlace(APIView):
    permission_classes = [AllowAny]  # Hamma comment qoldira oladi

    def post(self, request, place_id):
        place = RestPlace.objects.get(id=place_id)
        comment_text = request.data.get("comment", "").strip()

        if not comment_text:
            return Response({"error": "Comment cannot be empty."}, status=400)

        place.comments = f"{place.comments}\n{comment_text}" if place.comments else comment_text
        place.save()

        return Response({"message": "Comment added!"}, status=201)

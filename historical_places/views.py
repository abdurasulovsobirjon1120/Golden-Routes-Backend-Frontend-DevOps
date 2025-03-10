from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Country, Region, HistoricalPlace, Favourite
from .serializers import CountrySerializer, HistoricalPlaceSerializer
from .serializers import RegionListSerializer, RegionDetailSerializer
from rest_framework.permissions import AllowAny


# Country API
class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        """GET hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [AllowAny()]


# Region APIs
class RegionListView(generics.ListAPIView):
    """Barcha regionlarni qaytaradi"""
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer  # Faqat region ma'lumotlarini qaytaradi
    permission_classes = [AllowAny]

class RegionDetailView(generics.RetrieveAPIView):
    """Bitta region va unga tegishli historical placesni qaytaradi"""
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer  # To‘liq ma'lumot bilan qaytaradi
    permission_classes = [AllowAny]


# Historical Places APIs
class HistoricalPlaceListCreateView(generics.ListCreateAPIView):
    queryset = HistoricalPlace.objects.all()
    serializer_class = HistoricalPlaceSerializer

    def get_permissions(self):
        """GET hamma uchun ochiq, POST faqat adminlarga ruxsat"""
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [AllowAny()]


class HistoricalPlaceDetailView(generics.RetrieveAPIView):
    queryset = HistoricalPlace.objects.all()
    serializer_class = HistoricalPlaceSerializer
    permission_classes = [AllowAny]


# Favourite API
class FavouriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, place_id):
        place = get_object_or_404(HistoricalPlace, id=place_id)
        fav, created = Favourite.objects.get_or_create(user=request.user, place=place)
        return Response({"message": "Added to favourites!"} if created else {"message": "Already in favourites!"})

    def delete(self, request, place_id):
        fav = Favourite.objects.filter(user=request.user, place_id=place_id)
        if fav.exists():
            fav.delete()
            return Response({"message": "Removed from favourites!"})
        return Response({"error": "Not found in favourites!"}, status=400)


# Rating (Stars) API
class RateHistoricalPlace(APIView):
    permission_classes = [AllowAny]

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


# Comment API
class CommentHistoricalPlace(APIView):
    permission_classes = [AllowAny]

    def post(self, request, place_id):
        place = get_object_or_404(HistoricalPlace, id=place_id)
        comment_text = request.data.get("comment", "").strip()

        if not comment_text:
            return Response({"error": "Comment cannot be empty."}, status=400)

        place.comment = f"{place.comment}\n{comment_text}" if place.comment else comment_text
        place.save()

        return Response({"message": "Comment added!"}, status=201)

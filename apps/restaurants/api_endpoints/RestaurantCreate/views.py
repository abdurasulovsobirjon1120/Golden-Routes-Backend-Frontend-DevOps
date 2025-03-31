from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.restaurants.models import Restaurant
from .serializers import RestaurantCreateSerializer

class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = serializer.save()
        
        response_data = {
            "success": True,
            "message": "Restoran muvaffaqiyatli qo'shildi",
            "data": {
                "id": restaurant.id,
                "name": restaurant.name,
                "phone_number": restaurant.phone_number,
                "location": restaurant.location
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

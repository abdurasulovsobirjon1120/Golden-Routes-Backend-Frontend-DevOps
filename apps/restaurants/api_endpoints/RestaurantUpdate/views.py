from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.restaurants.models import Restaurant
from .serializers import RestaurantUpdateSerializer


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
            
        response_data = {
            "success": True,
            "message": "Restoran ma'lumotlari muvaffaqiyatli yangilandi",
            "data": {
                "id": instance.id,
                "updated_fields": list(request.data.keys())
            }
        }
        return Response(response_data, status=status.HTTP_200_OK)
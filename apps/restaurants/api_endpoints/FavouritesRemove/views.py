from rest_framework import permissions 
from apps.restaurants.models import Restaurant
from rest_framework.generics import DestroyAPIView

class RemoveFavouriteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

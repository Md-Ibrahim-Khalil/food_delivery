from .models import Restaurant
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import RestaurantSerializer
from authuser.models import IsStaff 

class RestaurantCreateView(CreateAPIView):
    permission_classes = [IsStaff]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

class RestaurantUpdateView(UpdateAPIView):
    permission_classes = [IsStaff]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
class RestaurantListView(ListAPIView):
    permission_classes = [IsStaff]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    
    
class RestaurantDeleteView(DestroyAPIView):
    permission_classes = [IsStaff]
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
from .models import Restaurant
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import MenuSerializer
from authuser.models import IsStaff 
from rest_framework.authentication import TokenAuthentication

class MenuCreateView(CreateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    queryset = Restaurant.objects.all()
    
class MenuUpdateView(UpdateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    queryset = Restaurant.objects.all()
    
class MenuListView(ListAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    queryset = Restaurant.objects.all()
    
class MenuDeleteView(DestroyAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = MenuSerializer
    queryset = Restaurant.objects.all()
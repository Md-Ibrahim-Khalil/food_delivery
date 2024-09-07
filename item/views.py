from .models import Item
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ItemSerializer
from authuser.models import IsStaff 
from rest_framework.authentication import TokenAuthentication

class ItemCreateView(CreateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class ItemUpdateView(UpdateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class ItemListView(ListAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class ItemDeleteView(DestroyAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
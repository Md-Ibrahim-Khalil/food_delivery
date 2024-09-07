from .models import Order
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import OrderSerializer
from authuser.models import IsStaff 
from rest_framework.authentication import TokenAuthentication

class OrderCreateView(CreateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
class OrderUpdateView(UpdateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
class OrderListView(ListAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
class OrderDeleteView(DestroyAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()        
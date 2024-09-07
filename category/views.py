from .models import Category
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import CategorySerializer
from authuser.models import IsStaff 
from rest_framework.authentication import TokenAuthentication

class CategoryCreateView(CreateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryUpdateView(UpdateAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryListView(ListAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDeleteView(DestroyAPIView):
    permission_classes = [IsStaff]
    authentication_classes = [TokenAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
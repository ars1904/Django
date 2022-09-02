from .models import Category, Articles
from .serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = PostSerializer
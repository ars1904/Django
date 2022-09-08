from django.urls import path, include
from .models import Category, Articles,Tag
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags=serializers.StringRelatedField(many=True)
    class Meta:
        model = Articles
        exclude=['user']
        #fields = '__all__'

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ViewSet):
   
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandViewSet(viewsets.ViewSet):

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ViewSet):

    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
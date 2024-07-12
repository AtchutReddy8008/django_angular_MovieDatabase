from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer

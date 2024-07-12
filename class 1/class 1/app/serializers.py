
from .models import Products
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Products
        fields="__all__"

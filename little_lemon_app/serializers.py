from .models import Catagory, MenuItem
from rest_framework import serializers


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'catagory', 'price', 'stock']
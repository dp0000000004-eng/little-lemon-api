from .models import Catagory, MenuItem
from rest_framework import serializers
from decimal import Decimal


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['id', 'slug', 'title']



class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    catagory = CatagorySerializer(read_only=True)
    price_after_task = serializers.SerializerMethodField(method_name="after_task")
    class Meta:
        model = MenuItem
        fields = ['id', 'catagory', 'price', 'stock', 'price_after_task']

    def after_task(self, product:MenuItem):
        return product.price * Decimal(1.1)
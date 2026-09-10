from .models import Catagory, MenuItem
from rest_framework import serializers
from decimal import Decimal
import bleach


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = ['id', 'slug', 'title']



class MenuItemSerializer(serializers.ModelSerializer):
    catagory = CatagorySerializer(read_only=True)
    price_after_task = serializers.SerializerMethodField(method_name="after_task")

    def validate_title(self, value):
        return bleach.clean(value)
    class Meta:
        model = MenuItem
        fields = ['id', 'catagory', 'price', 'stock', 'price_after_task']

        extra_kwargs = {
            "price":{
                "min_value":2
            },
            "stock":{
                "source":"inventory",
                "min_value":0
            }
        }

    def after_task(self, product:MenuItem):
        return product.price * Decimal(1.1)
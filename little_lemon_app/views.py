from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import response
from rest_framework.decorators import api_view, renderer_classes
from .serializers import MenuItemSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import MenuItem
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
@renderer_classes([ BrowsableAPIRenderer, JSONRenderer])
def menuItemsViews(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('catagory').all()
        itemSerializer = MenuItemSerializer(items, many=True)
        return Response(itemSerializer.data)
    if request.method == "POST":
        itemsSerializer = MenuItemSerializer(data=request.data)
        itemsSerializer.is_valid(raise_exception=True)
        itemsSerializer.save()
        return Response(itemSerializer.data, status.HTTP_201_CREATED)
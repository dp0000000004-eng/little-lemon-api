from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import response
from rest_framework.decorators import api_view, renderer_classes
from .serializers import MenuItemSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import MenuItem
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET', 'POST'])
@renderer_classes([ BrowsableAPIRenderer, JSONRenderer])
def menuItemsViews(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('catagory').all()

        catagory_name = request.query_params.get('catagory')
        price_to = request.query_params.get('price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')


        if catagory_name:
            items = items.filter(catagory__title=catagory_name)
        if price_to:
            items = items.filter(price=price_to)
        if search:
            items = items.filter(catagory__title__istartswith=search)
        if ordering:
            if ordering == "reversed__price":
                items = items.order_by("-price")
            elif ordering == "reversed__stock":
                items = items.order_by('-inventory')
            elif ordering == "reversed__title":
                items.order_by('-catagory__title')
            else:
                ordered_list = ordering.split(",")
                items = items.order_by(*ordered_list)


        itemsSerializer = MenuItemSerializer(items, many=True)
        return Response(itemsSerializer.data)
    
    if request.method == "POST":
        itemsSerializer = MenuItemSerializer(data=request.data)
        itemsSerializer.is_valid(raise_exception=True)
        itemsSerializer.save()
        return Response(itemsSerializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def singleMenuViews(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    itemSerializer = MenuItemSerializer(item)
    return Response(itemSerializer.data)
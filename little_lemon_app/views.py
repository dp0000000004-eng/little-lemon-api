from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import response
from rest_framework.decorators import api_view, throttle_classes, renderer_classes
from .serializers import MenuItemSerializer, CatagorySerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from .models import MenuItem, Catagory
from rest_framework import status
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .paginators import PaginatorPageLimt as Pagination
from .throttle import TenMinutesThrottle 

# Create your views here.


@api_view(['GET', 'POST'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def catagoryView(request):
    if request.method == 'GET':
        category = Catagory.objects.all()
        categorySerializer = CatagorySerializer(category, many=True)
        return Response(categorySerializer.data)
    if request.method == 'POST':
        postCatagorySerializer = CatagorySerializer(data=request.data, many=True)
        postCatagorySerializer.is_valid(raise_exception=True)
        postCatagorySerializer.save()
        return Response(postCatagorySerializer.data, status.HTTP_201_CREATED)



@api_view(['GET', 'POST', ])
@renderer_classes([BrowsableAPIRenderer,  JSONRenderer, TemplateHTMLRenderer])
def menuItemsViews(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('catagory').all()

        catagory_name = request.query_params.get('catagory')
        price_to = request.query_params.get('price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)


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


        if int(perpage) > Pagination.page_limit:
            return HttpResponseBadRequest(f"Error {HttpResponseBadRequest.status_code} The limit of per page data is {Pagination.page_limit}" )

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []


        itemsSerializer = MenuItemSerializer(items, many=True)
        return Response(
            {
                "items":itemsSerializer.data
            },
            template_name='data.html'
        )
    
    if request.method == "POST":
        itemsSerializer = MenuItemSerializer(data=request.data, many=True)
        itemsSerializer.is_valid(raise_exception=True)
        itemsSerializer.save()
        return Response(itemsSerializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def singleMenuViews(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    itemSerializer = MenuItemSerializer(item)
    if request.method == "DELETE":
        item.delete()
        return HttpResponse('Item deleted sussesfuly')
    return Response(itemSerializer.data)


@api_view(['GET', 'POST'])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
@permission_classes([IsAdminUser])
@throttle_classes([UserRateThrottle])
def hardcodedData(request):
    data = {
        "name":"Israt",
        "branch":"CE&IoT"
    }

    return Response(data)


@api_view()
@permission_classes([IsAuthenticated, IsAdminUser])
def secreate(request):
    return Response(
        {
            "name":"deba",
            "age":18
        }
    )



@api_view()
@permission_classes([IsAuthenticated])
def manager_only(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response(
            {
                "message":"This only show to manager"
            }
        )
    else:
        return Response(
            {"mesage":"You are not authorized"}, status.HTTP_403_FORBIDDEN
        )



@api_view()
@throttle_classes([AnonRateThrottle])
def anon_user(request):
    return Response(
        {
            "message":"This is for anon client"
        }
    )

@api_view()
@throttle_classes([TenMinutesThrottle])
@permission_classes([IsAuthenticated])
def user_client(request):
    return Response(
        {
            "message":"This is for Auth User client"
        }
    )
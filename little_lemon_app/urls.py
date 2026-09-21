from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.menuItemsViews, name="menu_items"),
    path('menu-items/<int:id>', views.singleMenuViews, name='singleMenu'),
    path('category/', views.catagoryView),
    path('data/', views.hardcodedData),
    path('s-msg/', views.secreate),
    path('auth-token-create/', obtain_auth_token),
    path('manager/', views.manager_only),
]
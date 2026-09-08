from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.menuItemsViews, name="menu_items"),
]
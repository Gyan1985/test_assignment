from django.contrib import admin
from django.urls import path
from .views import (
    InventoryDetailView, InventoryListView,
    InventoryListApiView
)


urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory-list'),
    path('api/inventory', InventoryListApiView.as_view(), name='inventory-api-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
]

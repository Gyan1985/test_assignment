from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from .models import Inventory
from .serializers import InventorySerializer


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_details.html'


class InventoryListView(TemplateView):
    template_name = 'landing.html'


class InventoryListApiView(ListAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.select_related('supplier')
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']

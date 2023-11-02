from rest_framework import serializers
from .models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['name']


class InventorySerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    class Meta:
        model = Inventory
        fields = [
            'id',
            'name',
            'availability',
            'supplier'
        ]

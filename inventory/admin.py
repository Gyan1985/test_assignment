from django.contrib import admin
from inventory.models import Inventory, Supplier


class InventoryAdmin(admin.ModelAdmin):
    model = Inventory


class SupplierAdmin(admin.ModelAdmin):
    model = Supplier


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Supplier, SupplierAdmin)

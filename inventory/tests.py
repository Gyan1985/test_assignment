from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Inventory, Supplier
from .serializers import InventorySerializer


class InventoryDetailViewTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create()
        self.inventory = Inventory.objects.create(
            name='Test Inventory',
            description='description',
            stock=1,
            availability=1,
            supplier=self.supplier,
        )

    def test_inventory_detail_view(self):
        url = reverse('inventory-detail', kwargs={'pk': self.inventory.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_details.html')

class InventoryListViewTest(TestCase):
    def test_inventory_list_view(self):
        url = reverse('inventory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

class InventoryListApiViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create()
        self.inventory = Inventory.objects.create(
            name='Test Inventory',
            description='description',
            stock=1,
            availability=1,
            supplier=self.supplier,
        )

    def test_inventory_list_api_view(self):
        url = reverse('inventory-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, InventorySerializer([self.inventory], many=True).data)

# tests.py
from django.test import TestCase
from django.utils import timezone
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorModelTest(TestCase):
    def test_vendor_creation(self):
        vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Contact details",
            address="Vendor Address",
            vendor_code="V001"
        )
        self.assertEqual(vendor.name, "Test Vendor")
        self.assertEqual(vendor.contact_details, "Contact details")
        self.assertEqual(vendor.address, "Vendor Address")
        self.assertEqual(vendor.vendor_code, "V001")
        self.assertEqual(vendor.on_time_delivery_rate, 0.0)  # Default value
        self.assertEqual(vendor.quality_rating_avg, 0.0)  # Default value
        self.assertEqual(vendor.average_response_time, 0.0)  # Default value
        self.assertEqual(vendor.fulfillment_rate, 0.0)  # Default value

class PurchaseOrderModelTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Contact details",
            address="Vendor Address",
            vendor_code="V001"
        )

    def test_purchase_order_creation(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number="PO001",
            vendor=self.vendor,
            expected_delivery_date=timezone.now(),
            items={"item": "Item description"},
            quantity=10,
            status='pending'
        )
        self.assertEqual(purchase_order.po_number, "PO001")
        self.assertEqual(purchase_order.vendor, self.vendor)
        self.assertIsNotNone(purchase_order.order_date)
        self.assertIsNotNone(purchase_order.expected_delivery_date)
        self.assertIsNone(purchase_order.delivery_date)
        self.assertEqual(purchase_order.items, {"item": "Item description"})
        self.assertEqual(purchase_order.quantity, 10)
        self.assertEqual(purchase_order.status, 'pending')
        self.assertIsNone(purchase_order.quality_rating)  # Null by default
        self.assertIsNotNone(purchase_order.issue_date)
        self.assertIsNone(purchase_order.acknowledgment_date)

    def test_save_method(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            expected_delivery_date=timezone.now(),
            items={"item": "Item description"},
            quantity=10,
            status='pending'
        )
        purchase_order.status = 'completed'
        purchase_order.save()
        self.assertIsNotNone(purchase_order.delivery_date)

class HistoricalPerformanceModelTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="Test Vendor",
            contact_details="Contact details",
            address="Vendor Address",
            vendor_code="V001"
        )

    def test_historical_performance_creation(self):
        historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.9,
            quality_rating_avg=4.5,
            average_response_time=2.3,
            fulfillment_rate=0.95
        )
        self.assertEqual(historical_performance.vendor, self.vendor)
        self.assertIsNotNone(historical_performance.date)
        self.assertEqual(historical_performance.on_time_delivery_rate, 0.9)
        self.assertEqual(historical_performance.quality_rating_avg, 4.5)
        self.assertEqual(historical_performance.average_response_time, 2.3)
        self.assertEqual(historical_performance.fulfillment_rate, 0.95)
